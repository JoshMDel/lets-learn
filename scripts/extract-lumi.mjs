// Cuts the individual Lumi poses out of design/lumi-concept-sheet.png into
// transparent WebP files in public/brand/lumi/. The concept sheet sits on a
// near-black background, so each pose is cropped and the background removed
// by flood-filling inward from the crop edge (so dark pixels *inside* a pose,
// like the book or the card, are kept). Run: node scripts/extract-lumi.mjs
import sharp from 'sharp'
import { mkdir } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), '..')
const sheet = path.join(root, 'design', 'lumi-concept-sheet.png')
const outDir = path.join(root, 'public', 'brand', 'lumi')
await mkdir(outDir, { recursive: true })

// Crop boxes (x0, y0, x1, y1) found by connected-component analysis of the sheet.
const POSES = {
  'lumi-welcome': [752, 100, 1342, 600], // waving, holding an open book
  'lumi-celebrating': [612, 648, 968, 938], // arms up, cheering
  'lumi-thinking': [1130, 596, 1448, 940], // hand on chin, lightbulb
  'lumi-pointing': [88, 630, 552, 940], // pointing at a card
}
// The card in lumi-pointing is nearly the same colour as the sheet background,
// so it's kept opaque as a rounded rect instead of being flood-filled away.
// Sheet coordinates: [x0, y0, x1, y1, cornerRadius].
const KEEP = { 'lumi-pointing': [[352, 634, 548, 850, 26]] }
const BG = [11, 16, 21]
const TOL = 52

const { data: src, info } = await sharp(sheet).ensureAlpha().raw().toBuffer({ resolveWithObject: true })

for (const [name, [x0, y0, x1, y1]] of Object.entries(POSES)) {
  const w = x1 - x0
  const h = y1 - y0
  const px = new Uint8Array(w * h * 4)
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      const s = ((y0 + y) * info.width + (x0 + x)) * 4
      const d = (y * w + x) * 4
      px[d] = src[s]; px[d + 1] = src[s + 1]; px[d + 2] = src[s + 2]; px[d + 3] = 255
    }
  }
  const dist = (i) => Math.max(Math.abs(px[i * 4] - BG[0]), Math.abs(px[i * 4 + 1] - BG[1]), Math.abs(px[i * 4 + 2] - BG[2]))
  // flood-fill background from the crop edge
  const bg = new Uint8Array(w * h)
  const stack = []
  const seed = (x, y) => { const i = y * w + x; if (!bg[i] && dist(i) < TOL) { bg[i] = 1; stack.push(i) } }
  for (let x = 0; x < w; x++) { seed(x, 0); seed(x, h - 1) }
  for (let y = 0; y < h; y++) { seed(0, y); seed(w - 1, y) }
  while (stack.length) {
    const i = stack.pop()
    const x = i % w, y = (i / w) | 0
    if (x > 0) seed(x - 1, y)
    if (x < w - 1) seed(x + 1, y)
    if (y > 0) seed(x, y - 1)
    if (y < h - 1) seed(x, y + 1)
  }
  for (const [kx0, ky0, kx1, ky1, r] of KEEP[name] ?? []) {
    for (let y = ky0 - y0; y < ky1 - y0; y++) for (let x = kx0 - x0; x < kx1 - x0; x++) {
      if (x < 0 || y < 0 || x >= w || y >= h) continue
      const cx = Math.min(Math.max(x, kx0 - x0 + r), kx1 - x0 - r)
      const cy = Math.min(Math.max(y, ky0 - y0 + r), ky1 - y0 - r)
      if ((x - cx) ** 2 + (y - cy) ** 2 <= r * r) bg[y * w + x] = 0
    }
  }
  // erode the kept area by 1px (drops the dark fringe), then soften the edge
  const keep = new Uint8Array(w * h)
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    let ok = 1
    for (let dy = -1; dy <= 1 && ok; dy++) for (let dx = -1; dx <= 1; dx++) {
      const nx = x + dx, ny = y + dy
      if (nx < 0 || ny < 0 || nx >= w || ny >= h) continue
      if (bg[ny * w + nx]) { ok = 0; break }
    }
    keep[y * w + x] = ok
  }
  let minX = w, minY = h, maxX = 0, maxY = 0
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    let sum = 0, n = 0
    for (let dy = -1; dy <= 1; dy++) for (let dx = -1; dx <= 1; dx++) {
      const nx = x + dx, ny = y + dy
      if (nx < 0 || ny < 0 || nx >= w || ny >= h) continue
      sum += keep[ny * w + nx]; n++
    }
    const a = Math.round((sum / n) * 255)
    px[(y * w + x) * 4 + 3] = a
    if (a > 8) { if (x < minX) minX = x; if (x > maxX) maxX = x; if (y < minY) minY = y; if (y > maxY) maxY = y }
  }
  await sharp(Buffer.from(px), { raw: { width: w, height: h, channels: 4 } })
    .extract({ left: minX, top: minY, width: maxX - minX + 1, height: maxY - minY + 1 })
    .webp({ quality: 90, alphaQuality: 100 })
    .toFile(path.join(outDir, `${name}.webp`))
  console.log('wrote', name, `${maxX - minX + 1}x${maxY - minY + 1}`)
}

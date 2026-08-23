// One-off icon generator: rasterizes scripts/icon-source.svg into every PNG
// size the PWA manifest / iOS home screen needs. Run with `node scripts/generate-icons.mjs`.
import sharp from 'sharp'
import { mkdir } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const src = path.join(__dirname, 'icon-source.svg')
const outDir = path.join(__dirname, '..', 'public', 'icons')

await mkdir(outDir, { recursive: true })

const targets = [
  { name: 'icon-192.png', size: 192 },
  { name: 'icon-512.png', size: 512 },
  { name: 'icon-maskable-512.png', size: 512 },
  { name: 'apple-touch-icon.png', size: 180 },
]

for (const { name, size } of targets) {
  await sharp(src, { density: 384 })
    .resize(size, size)
    .png()
    .toFile(path.join(outDir, name))
  console.log('wrote', name)
}

// Also drop a simplified favicon.svg at the app root (browsers render this
// directly, no rasterization needed).

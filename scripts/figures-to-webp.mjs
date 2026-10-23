// Converts the PNG crops written by content/grade6-afrikaans-book2/tools/crop_figure.py into WebP (and removes the PNGs).
import sharp from 'sharp'
import { readdirSync, unlinkSync } from 'node:fs'
const dir = 'public/workbook/gr6-afr-b2/figures'
for (const f of readdirSync(dir).filter((x) => x.endsWith('.png'))) {
  await sharp(`${dir}/${f}`).webp({ quality: 80 }).toFile(`${dir}/${f.replace('.png', '.webp')}`)
  unlinkSync(`${dir}/${f}`)
  console.log('wrote', f.replace('.png', '.webp'))
}

"""Cut a figure out of a workbook PDF page into public/workbook/gr6-afr-b2/figures/<name>.webp

    python crop_figure.py NAME PDF_PAGE X0 Y0 X1 Y1

X/Y are pixels on the 820-px-wide page render (the same coordinates you see in public/workbook/gr6-afr-b2/pNNN.webp).
Needs PyMuPDF and the two workbook PDFs (set WORKBOOK_DIR if they are not in ~/Downloads/Grade_6_Afrikaans_Workbook_Files).
"""
import io
import os
import sys

import pymupdf

WB = os.environ.get('WORKBOOK_DIR', os.path.expanduser('~/Downloads/Grade_6_Afrikaans_Workbook_Files'))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'public', 'workbook', 'gr6-afr-b2', 'figures')


def page(n):
    if n <= 69:
        return pymupdf.open(os.path.join(WB, 'Gr6_Afrikaans_Workbook_Part_1_pages_1-69.pdf'))[n - 1]
    return pymupdf.open(os.path.join(WB, 'Gr6_Afrikaans_Workbook_Part_2_pages_70-138.pdf'))[n - 70]


def crop(name, pdf_page, x0, y0, x1, y1, width=720):
    pg = page(pdf_page)
    k = pg.rect.width / 820.0
    clip = pymupdf.Rect(x0 * k, y0 * k, x1 * k, y1 * k)
    zoom = width / clip.width
    pix = pg.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), clip=clip, alpha=False)
    os.makedirs(OUT, exist_ok=True)
    png = os.path.join(OUT, name + '.png')
    pix.save(png)
    return png


if __name__ == '__main__':
    name, pg, *box = sys.argv[1:]
    print(crop(name, int(pg), *map(float, box)))

from django.core.files.storage import FileSystemStorage

import pathlib
import os

from PIL import Image

path = os.path.join(pathlib.Path(__file__).parent.parent.parent, 'media')

def batchit(files):
    batchit_to = []
    for f in files:
        fs = FileSystemStorage()
        img = Image.open(f)
        img = img.convert('L')
        img.save(f'{path}/{f.name}')
        batchit_to.append(fs.url(f.name))
    return batchit_to
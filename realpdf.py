from io import BytesIO
from PIL import Image
from zipfile import ZipFile

imgarr = []
def pdftime(mode, files):
    '''convert to pdf and return'''
    for i in range(len(files)) if mode == "onetoone" else range(len(files) - 1, -1, -1):
        image = Image.open(BytesIO.read(files[i]))



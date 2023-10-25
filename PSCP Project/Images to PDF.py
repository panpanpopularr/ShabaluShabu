import os
from PIL import Image
output = './PDFs'
source = './Images'

for file in os.listdir(source):
    if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
        image = image.open(os.path.join(source, file))
        image_changed = image.convert('RGB')
        image_changed.save(os.path.join(output, '{0}.pdf'.format(file.split('.'[-2]))))

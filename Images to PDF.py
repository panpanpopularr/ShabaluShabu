import os
from PIL import Image

output = "./PDFs"
source = './Images'
if not os.path.exists(output):
    os.makedirs(output) 

for file in os.listdir("./Images"):
    if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):

        image = Image.open(os.path.join(source, file))
        image_changed = image.convert('RGB')
        
        image_changed.save(output + '\\' + file.split('.')[0] + ".pdf")

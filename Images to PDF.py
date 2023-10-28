import os
from PIL import Image

output = "./PDFs"
source = './Images'
print(os.getcwd() )
for file in os.listdir("./Images"):
    print(os.path.join(output, '{0}.pdf'.format(file.split('.')[0])))
    if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
        print(os.path.join(source, file))

        image = Image.open(os.path.join(source, file))
        image_changed = image.convert('RGB')
        if not os.path.exists(output):
            os.makedirs(output) 
        image_changed.save(output + '\\' + file.split('.')[0] + ".pdf")

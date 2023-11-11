import os
from PIL import Image

output = "./PDFs"
source = './Images'
imgarr = []
# จะให้มันเป็นแบบ 1ต่อ1 ให้เปลี่ยนเป็น onetoone แต่ถ้าจะเอาแบบทุกอันเป็นไฟล์เดียวใช้ allinone
if not os.path.exists(output):
    os.makedirs(output) 
def pdfmaker(mode):
    for file in os.listdir("./Images") if mode != "allinone" else reversed(os.listdir(source)):
        if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):

            image = Image.open(os.path.join(source, file))
            image_changed = image.convert('RGB')
            if mode == "allinone":
                print(file)
                imgarr.append(image_changed)
            else:
                image_changed.save(output + '\\' + file.split('.')[0] + ".pdf")
    if mode == "allinone":
        imgarr.pop(-1)
        image_changed.save(output + '\\' + "Test.pdf", save_all=True, append_images=reversed(imgarr))
pdfmaker('allinone')

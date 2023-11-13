import os
from io import BytesIO
from PIL import Image
from zipfile import ZipFile

output = "./PDFs"
source = './Images'
imgarr = []
# จะให้มันเป็นแบบ 1ต่อ1 ให้เปลี่ยนเป็น onetoone แต่ถ้าจะเอาแบบทุกอันเป็นไฟล์เดียวใช้ allinone
if not os.path.exists(output):
    os.makedirs(output) 
def pdfmaker(mode):
    for file in os.listdir(source) if mode != "allinone" else reversed(os.listdir(source)):
        if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):

            image = Image.open(os.path.join(source, file))
            image_changed = image.convert('RGB')
            if mode == "allinone":
                imgarr.append(image_changed)
            else:
                image_changed.save(output + '\\' + file.split('.')[0] + ".pdf")
    if mode == "allinone":
        imgarr.pop(-1)
        image_changed.save(output + '\\' + "Test.pdf", save_all=True, append_images=reversed(imgarr))
    else:
        folder_to_zip = './PDFs'
        zip_file_name = 'archive.zip'
        def zip_folder(folder_path, zip_name):
            with ZipFile(zip_name, 'w') as zipf:
                for foldername, sss, filenames in os.walk(folder_path):
                    print(foldername, filenames, sss)
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname)
        zip_folder(folder_to_zip, zip_file_name)
pdfmaker('onetoone')

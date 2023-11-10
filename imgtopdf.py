import os
import img2pdf

directory_path = "./Images"

image_files = [i for i in os.listdir(directory_path) if i.rfind(".jpg") if i.rfind(".jpeg") if i.rfind(".png")]
print(image_files)
pdf_data = img2pdf.convert(image_files)

with open("output.pdf", "wb") as file:
    file.write(pdf_data)
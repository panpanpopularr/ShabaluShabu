import os
import img2pdf

directory_path = "./img2pdf"

image_files = [i for i in os.listdir(directory_path) if i.endswith(".jpg") if i.endswith(".jpeg") if i.endswith(".png")]

pdf_data = img2pdf.convert(image_files)

with open("output.pdf", "wb") as file:
    file.write(pdf_data)
from PIL import Image
from io import BytesIO
from reportlab.pdfgen import canvas
import zipfile
import os


def pdftime(mode="allinone", files=None):
    '''convert to pdf and return'''
    def creator(files):
        pdf_bytesio = BytesIO()
        pdf_canvas = canvas.Canvas(pdf_bytesio)
        for i in range(len(files)):
            image = Image.open(BytesIO(files[list(files.keys())[i]].read()))
            width, height = image.size
            
            pdf_canvas.setPageSize((width, height))
            pdf_canvas.drawInlineImage(image, 0, 0, width=width, height=height)
            if i < len(files) - 1:
                pdf_canvas.showPage()
        pdf_canvas.save()
        pdf_bytesio.seek(0)
        return pdf_bytesio.getvalue()


    if mode == "allinone":
        return creator(files)
    else:
        zip_bytesio = BytesIO()
        with zipfile.ZipFile(zip_bytesio, 'w') as zip_file:
            for i in files:
                pdf_filename = f'{i.split(".")[0]}.pdf'
                print(pdf_filename)
                zip_file.writestr(pdf_filename, creator({i: files[i]}))

        zip_bytesio.seek(0)
        return zip_bytesio.getvalue()

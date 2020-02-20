import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pdf = wi(filename="test.pdf", resolution=300)
pdfImg = pdf.convert('jpeg')

imgBlobs = []
print("1")
for img in pdfImg.sequence:
    page = wi(image=img)
    imgBlobs.append(page.make_blob('jpeg'))

extracted_text = ""
print("2")
for imgBlob in imgBlobs:
    im = Image.open(io.BytesIO(imgBlob))
    text = pytesseract.image_to_string(im, lang='eng')
    extracted_text += text

print(extracted_text)

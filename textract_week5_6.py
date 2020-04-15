filename = 'sample.pdf'
pdfFileObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
if text != "":
    text = text
else:
    text = textract.process(fileurl, method='tesseract', language='eng')

print(text)

f = open("extracted_text.txt", "w", encoding='utf-8')
f.write(text)
print("Done!")
f.close()

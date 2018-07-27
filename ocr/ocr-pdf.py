import PyPDF2
#pdfFileObj = open('/home/julio/Documents/off_letter.pdf', 'rb')
pdfFileObj = open('off_letter.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print pdfReader.numPages
pageObj = pdfReader.getPage(0)
print pageObj.extractText()
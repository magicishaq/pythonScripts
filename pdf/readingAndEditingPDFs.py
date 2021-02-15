import PyPDF2
import os
os.chdir('C:\\Users\\ikhan\\Documents\\learningPython\\pdf')
pdfFile = open('cv.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile) #reader object

reader.numPages








# for pageNum in range(reader.numPages):
#     print(reader.getPage(pageNum).extractText())


#Writing to a pdf

pdf1 = open('cv.pdf' 'rb')
pdf2 = open('sonnets.pdf', 'rb')

#create two reader objects
reader1 = PyPDF2.PdfFileReader(pdf1)
reader2 = PyPDF2.PdfFileReader(pdf2)

#create a loop that adds pages to a new pdf file
writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.add(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.add(page)


#now the writer object has contents from both pdf files
combinedFile = open('combined.pdf' , 'wb')

writer.write(combinedFile)
combinedFile.close()
pdf1.close()
pdf2.close()


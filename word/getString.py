import docx,os
os.chdir('C:\\Users\\ikhan\\Documents\\learningPython\\word')


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
letter = getText('C:\\Users\\ikhan\\Documents\\learningPython\\word\Letter.docx')

print(letter)

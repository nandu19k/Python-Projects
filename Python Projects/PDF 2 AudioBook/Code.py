import pyttsx3
import PyPDF2

book = open("US_Declaration.pdf" , 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()

for num in range(0 , pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    print(text)
    speaker.say(text)
    speaker.runAndWait()
    

    
import magic
import PyPDF2
from PyPDF2 import PdfReader


class ReadFile:

    def exec(self, file):
        self.check_type(file)
        return self.read_file(file)

    def check_type(self, file):
        if ("PDF document" in magic.from_file(file)):
            return True
        else:
            raise ValueError("wrong type of file, pdf only")

    def read_file(self, file):
        f = open(file, 'rb')
        pageone = PyPDF2.PdfFileReader(f).getPage(0).extractText()
        text = ""
        for i in range(1, PyPDF2.PdfFileReader(f).getNumPages()):
            text += PyPDF2.PdfFileReader(f).getPage(i).extractText()
        f.close()
        return pageone, text
        
        
        
        """ class ReadFile:

    def exec(self, file):
        self.check_type(file)
        return self.read_file(file)

    def check_type(self, file):
        if ("PDF document" in magic.from_file(file)):
            return True
        else:
            raise ValueError("wrong type of file, pdf only")

    def read_file(self, file):
        f = open(file, 'rb')
        pdfReader = PdfReader(f)
        pageone = PyPDF2.PdfReader(f).pages[0].extract_text()
        text = ""
        for i in range(1, len(pdfReader.pages)):
            text += PyPDF2.PdfReader(f).pages[i].extract_text()
        f.close()
        return pageone, text """

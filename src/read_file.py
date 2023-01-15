import magic
import PyPDF2



class Read_File:

    def exec(self, file):
        self.check_type(file)
        return self.read_file(file)

    def check_type(self, file):
        if (magic.from_file(file) == "ASCII text, with CRLF line terminators" or 
            magic.from_file(file) == "ASCII text, with no line terminators" or
            "PDF document" in magic.from_file(file)):
            return True
        else:
            raise ValueError("wrong type of file, doc, docx, pdf, or txt only")

    def read_file(self, file):
        f = open(file, 'rb')
        text = PyPDF2.PdfFileReader(f).getPage(0).extractText()
        f.close()
        return text
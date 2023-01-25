import magic
import PyPDF2



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
        text = PyPDF2.PdfFileReader(f).getPage(0).extractText()
        f.close()
        return text
import magic
import docx
import os



class Find_Admin:

    def exec(self, file):
        self.check_type(file)
        return self.read_file(file)

    def check_type(self, file):
        if (magic.from_file(file) == "ASCII text, with CRLF line terminators" or 
            magic.from_file(file) == "ASCII text, with no line terminators"):
            return True
        else:
            raise ValueError("wrong type of file, doc, docx, or txt only")

    def read_file(self, file):
        document = docx.Document(os.path.abspath(file))
        content = []
        for paragraphs in document.paragraphs:
            content.append(paragraphs.text)
        return '\n'.join(content)

x = Find_Admin()
print(x.exec("word.docx"))
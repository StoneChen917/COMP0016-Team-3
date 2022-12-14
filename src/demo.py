import magic



class Find_Admin:

    def exec(self, file):
        print(self.check_type(file))

    def check_type(self, file):
        if (magic.from_file(file) == "ASCII text, with CRLF line terminators" or 
            magic.from_file(file) == "ASCII text, with no line terminators"):
            return True
        else:
            return False

x = Find_Admin()
x.exec("word.docx")
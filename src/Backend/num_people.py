from readfile import Read_File



class Num_People:

    def exec(self, file):
        file_text = Read_File().exec(file)
        return self.clean_up(self.get_num(file_text))

    def get_num(self, file_text):
        start = self.find_str(file_text, "Number of people affected: ")

        i = start
        while file_text[i] != " ":
            i += 1
        
        return file_text[start:i]

    def find_str(self, file_text, char):
        index = 0

        if char in file_text:
            c = char[0]
            for ch in file_text:
                if ch == c:
                    if file_text[index:index+len(char)] == char:
                        return index+len(char)

                index += 1

        return -1

    def clean_up(self, text):
        return text.replace(',', '')

print(Num_People().exec("sample1.pdf"))

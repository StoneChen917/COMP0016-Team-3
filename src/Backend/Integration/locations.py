import spacy
from readfile import ReadFile

class Locations():
    
    def __init__(self, file):
        self.file = file
        self.locations = self.exctract_loc()
    
    def exctract_loc(self):   
        nlp = spacy.load("en_core_web_lg")

        reader = ReadFile()
        first_page = reader.exec(self.file)[0]

        doc = nlp(first_page)

        locations = []
        for ent in doc.ents:
            if ent.label_ == "GPE":
                locations.append(ent.text)

        # Remove duplicate locations

        clean = []
        for i in locations:
            # print (type(i))
            if i not in clean:
                clean.append(i)
        # print(clean)

        return clean

test = Locations("MDRKH001final.pdf")
print(test.locations)


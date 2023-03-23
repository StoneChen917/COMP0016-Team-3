import spacy
from readfile import ReadFile

class Locations():
    """Gets a list of goepolitical entities in text, with duplicates removed"""
    def __init__(self, file):
        self.file = file
        self.locations = self.exctract_loc()


    def exctract_loc(self):   
        # load spaCy model
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
            if i not in clean:
                clean.append(i)

        return clean

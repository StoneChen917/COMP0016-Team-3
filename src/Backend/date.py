import readfile
import re
from datetime import datetime
import spacy
from readfile import Read_File
  
class date:

    #reading file into file_text
    def exec(self, file):
        file_text = Read_File().exec(file)
        return self.get_date(file_text)
    
    #printing text and label for each date
    def get_date(self, file_text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(file_text)
        for ent in doc.ents:
            print(ent.text, ent.label_)

#printing result
print(date().exec("sample1.pdf"))  


# searching string 
#match_str = re.search(r'\d{4}-\d{2}-\d{2}', test_str)
  
# computed date
# feeding format
#res = datetime.strptime(match_str.group(), '%Y-%m-%d').date()


#def normaize_date(date: str) -> datetime:
 #   try:
  #      d = parser.parse(date)
   #     return(d.strftime("%Y-%m-%d %H:%M:%S"))
    #except:  # anti-pattern, add missing exception type
     #   return date
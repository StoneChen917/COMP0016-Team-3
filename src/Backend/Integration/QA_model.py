from transformers import AutoModelForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline
from readfile import ReadFile

model = AutoModelForQuestionAnswering.from_pretrained('deepset/roberta-base-squad2')
tokenizer = AutoTokenizer.from_pretrained('deepset/roberta-base-squad2')

class qaModel():
    """
    Uses Question-Answering model to extract answers. Answers are stored in dictionary called self.answers
    """
    def __init__(self, file):
        self.file = file
        self.questions=["What is the Country of Disaster?",
        "What is the Operation Start Date?", 
        "What is the Operation End Date?",
        "What is the number of people affected?", 
        "What is the number of people assisted?", 
        "What is the Glide Number?", 
        "What is the Operation n°?", 
        "What is the Operation Budget?", 
        "What is the Host National Society?"]
        self.answers = {}
        self.extract_ans()
    
    def extract_ans(self):
        # get first page of document
        reader = ReadFile()
        first_page = reader.exec(self.file)[0]
        context = first_page

        # loop through questions
        for n in self.questions:
            tokenizer.encode(n, truncation = True, padding = True)
            tokenizer.encode('[CLS]')
            nlp = pipeline('question-answering', model = model, tokenizer = tokenizer)
            answer = nlp({'question': n, 'context': context})['answer']
            self.answers[n] = str(answer)


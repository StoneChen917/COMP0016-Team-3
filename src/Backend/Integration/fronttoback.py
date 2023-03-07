#from new_integ import main



class Frontoback():
    
    def __init__(self):
        self.files = []
        self.answers = {}

    def extract_answers(self):
        integ = main(self.files)
        answers = integ.final_extract
        self.answers = answers
    
    def set_files(self, files):
        for file in files:
            self.files.append(file)
        
    def get_admin0(self):
        x = self.answers["Country"]
        return x

    def get_iso(self):
        x = self.answers["iso"]
        return x
    
    def get_admin1(self):
        x = self.answers[["Admin1"]]
        return x
    
    def get_admin2(self):
        x = self.answers["Admin2"]
        return x
    
    def get_start(self):
        x = self.answers["Start"]
        return x
    
    def get_end(self):
        x = self.answers["End"]
        return x
    
    def get_glide(self):
        x = self.answers["Glide"]
        return x
    
    def get_operation_number(self):
        x = self.answers["OpBud"]
        return x

    def get_operation_budget(self):
        x = self.answers["OpBud"]
        return x
    
    def get_host(self):
        x = self.answers["Host"]
        return x
    
    def get_affected(self):
        x = self.answers["Affected"]
        return x

    def get_assisted(self):
        x = self.answers["Assisted"]
        return x  
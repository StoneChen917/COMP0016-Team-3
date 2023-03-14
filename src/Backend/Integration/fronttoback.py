import new_integ



class Frontoback():
    
    def __init__(self):
        self.files = []
        self.answers = []
        self.finished = False
        self.max = 0

    def extract_answers(self):
        integ = (self.files)
        self.answers = integ.final_extract
        self.max = len(self.answers) - 1
        self.finished = True

    def reset_ftb(self):
        self.finished = False
        self.files = []
        self.answers = []
        self.max = 0

    def is_finished(self):
        return self.finished

    def get_files(self):
        return self.files

    def get_answers(self):
        return self.answers

    def is_finished(self):
        return self.finished
    
    def get_max(self):
        return self.max
    
    def set_files(self, files):
        for file in files:
            self.files.append(file)
        
    def get_admin0(self, i):
        x = self.answers[i]["Country"]
        return x

    def get_iso(self, i):
        x = self.answers[i]["iso"]
        return x
    
    def get_admin1(self, i):
        x = self.answers[i]["Admin1"]
        return x
    
    def get_admin2(self, i):
        x = self.answers[i]["Admin2"]
        return x
    
    def get_start(self, i):
        x = self.answers[i]["Start"]
        return x
    
    def get_end(self, i):
        x = self.answers[i]["End"]
        return x
    
    def get_glide(self, i):
        x = self.answers[i]["Glide"]
        return x
    
    def get_operation_number(self, i):
        x = self.answers[i]["OpNum"]
        return x

    def get_operation_budget(self, i):
        x = self.answers[i]["OpBud"]
        return x
    
    def get_host(self, i):
        x = self.answers[i]["Host"]
        return x
    
    def get_affected(self, i):
        x = self.answers[i]["Affected"]
        return x

    def get_assisted(self, i):
        x = self.answers[i]["Assisted"]
        return x  
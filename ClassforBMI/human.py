class Human:
    def __init__(self,h=0,w=0):
        self.height = h
        self.weight = w
    def BMI(self):
        return self.weight/(self.height/100)**2
    def health(self):
        if self.BMI()> 25:
            return '過重'
        elif self.BMI() <18:
            return '過輕'
        else:
            return '正常'


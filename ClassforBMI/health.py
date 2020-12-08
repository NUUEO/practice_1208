class Human:
    def __init__(self,h=0,m=0):
        self.height = h
        self.weight = m
    def BMI(self):
        return self.weight/(self.height/100)**2
    def BMItype(self,maxmum=25,minmum=18):
        if self.BMI()> maxmum:
            return '過重'
        elif self.BMI() <minmum:
            return '過輕'
        else:
            return '正常'
            
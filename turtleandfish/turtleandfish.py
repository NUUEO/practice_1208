import random
class Animal(object):
    """
    將烏龜和魚的共同特性抽象出來的類
    """
    def __init__(self):
        self.x = random.randint(1,10)
        self.y = random.randint(1,10)

    def move(self,move_skill):
        new_x = self.x + random.choice(move_skill)
        new_y = self.y + random.choice(move_skill)
        self.x = self.is_vaild(new_x)
        self.y = self.is_vaild(new_y)

    def is_vaild(self,value):
        if 1 <= value <= 10:
            return value
        elif value<1:
            return abs(value)
        elif value >10:
            return 10-(value-10)


class Turtle(Animal):

    def __init__(self):
        super(Turtle,self).__init__()
        self.power=100

    def move(self,move_skill= (-2,-1,0,1,2)):
        super(Turtle,self).move(move_skill)
        self.power -= 1
    def eat(self):
        self.power += 20

class Fishs(Animal):

    def move(self,move_skill=(-1,0,1)):
        super(Fishs,self).move(move_skill)

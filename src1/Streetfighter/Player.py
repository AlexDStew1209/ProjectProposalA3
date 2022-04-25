#By Alex Stewart

class Player:
    #Member Variables
    x = 0
    y = 0
    health = 100
    lives = 3
    pColor1 = 0
    pColor2 = 0
    pColor3 = 0
    #Constructor
    def __init__(self,x,y,pColor1,pColor2,pColor3):
        self.x = x
        self.y = y
        self.pColor2 = pColor2
        self.pColor1 = pColor1
        self.pColor3 = pColor3
    #Methods
    def display(self):
        fill(self.pColor1,self.pColor2,self.pColor3)
        rect(self.x,self.y,100,200)
        

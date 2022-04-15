class Player:
    #Member Variables
    x = 0
    y = 0
    health = 100
    lives = 3
    pColor = 0
    #Constructor
    def __init__(self,x,y,pColor):
        self.x = x
        self.y = y
        self.pColor = pColor
    #Methods
    def display(self):
        fill(self.pColor)
        rect(x,y,25,50)
        


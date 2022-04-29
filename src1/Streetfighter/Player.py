#By Alex Stewart

class Player:
    #Member Variables
    x = 0
    y = 0
    health = 100
    lives = 3
    directionRight = True
    #Constructor
    def __init__(self,x,y,pNum):
        self.x = x
        self.y = y
        self.health = 100
        self.lives = 3
        self.directionRight = True
        self.pNum = pNum
    #Methods
    def display(self):
        if self.pNum == 1:
            pRight = loadImage("p1Right.png")
            pLeft = loadImage("p1Left.png")
        elif self.pNum == 2:
            pRight = loadImage("p2Right.png")
            pLeft = loadImage("p2Left.png")
        if self.directionRight == True:
            image(pRight,self.x,self.y)
        elif self.directionRight == False:
            image(pLeft,self.x,self.y)
            
        
    def moveRight(self):
        self.x += 7
        self.directionRight = True
        
    def moveLeft(self):
        self.x -= 7
        self.directionRight = False
        
    def moveUp(self):
        self.y -= 5
        
    
        

#By Alex Stewart

class Player:
    #Member Variables
    x = 0
    y = 0
    health = 100
    lives = 3
    directionRight = 1
    pNum = 1
    #Constructor
    def __init__(self,x,y,pNum):
        self.x = x
        self.y = y
        self.health = 100
        self.lives = 3
        self.pDirection = 1
        self.pNum = pNum
    #Methods
    def display(self):
        if self.pNum == 1:
            pRight = loadImage("p1Right.png")
            pLeft = loadImage("p1Left.png")
            pPunchR = loadImage("p1punchR.png")
            pPunchL = loadImage("p1punchL.png")
        elif self.pNum == 2:
            pRight = loadImage("p2Right.png")
            pLeft = loadImage("p2Left.png")
            pPunchR = loadImage("p2punchR.png")
            pPunchL = loadImage("p2punchL.png")
        if self.pDirection == 1:
            image(pRight,self.x,self.y)
        elif self.pDirection == 2:
            image(pLeft,self.x,self.y)
        elif self.pDirection == 3:
            image(pPunchR,self.x,self.y)
        elif self.pDirection == 4:
            image(pPunchL,self.x,self.y)
            
        
    def moveRight(self):
        self.x += 7
        self.pDirection = 1
        
    def moveLeft(self):
        self.x -= 7
        self.pDirection = 2
        
    def moveUp(self):
        self.y -= 5
        
    def attack(self):
        if self.pDirection == 1 or self.pDirection == 3:
            self.pDirection = 3
        if self.pDirection == 2 or self.pDirection == 4:
            self.pDirection = 4 
        
        
    
        

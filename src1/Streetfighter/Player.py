#By Alex Stewart

class Player:
    #Member Variables
    x = 0
    y = 0
    health = 100
    deaths = 0
    directionRight = 1
    pNum = 1
    damage = 10
    #Constructor
    def __init__(self,x,y,pNum):
        self.x = x
        self.y = y
        self.health = 100
        self.deaths = 0
        self.pDirection = 1
        self.pNum = pNum
        self.damage = 10
    #Methods
    def display(self):
        if self.pNum == 1:
            pRight = loadImage("p1Right.png")
            pLeft = loadImage("p1Left.png")
            pPunchL = loadImage("p1punchL.png")
            pPunchR = loadImage("p1punchR.png")
        elif self.pNum == 2:
            pRight = loadImage("p2Right.png")
            pLeft = loadImage("p2Left.png")
            pPunchL = loadImage("p2punchL.png")
            pPunchR = loadImage("p2punchR.png")
        if self.pDirection == 1:
            image(pRight,self.x,self.y)
        elif self.pDirection == 2:
            image(pLeft,self.x,self.y)
        elif self.pDirection == 3:
            image(pPunchR,self.x,self.y)
        elif self.pDirection == 4:
            image(pPunchL,self.x,self.y)

    def down(self):
        self.y += 3
        
    def moveRight(self):
        self.x += 15
        self.pDirection = 1
        
    def moveLeft(self):
        self.x -= 15
        self.pDirection = 2
        
    def moveUp(self):
        self.y -= 30
        
    def attack(self):
        if self.pDirection == 1 or self.pDirection == 3:
            self.pDirection = 3
        elif self.pDirection == 2 or self.pDirection == 4:
            self.pDirection = 4 
        
        
    
        

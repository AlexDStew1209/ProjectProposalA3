#By Alex Stewart

class Player:
    #Member Variables
    x = 0
    y = 0
    health = 100
    lives = 3
    directionRight = True
    #Constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.health = 100
        self.lives = 3
        self.directionRight = True
    #Methods
    def display(self):
        p1Right = loadImage("p1Right.png")
        p1Left = loadImage("p1Left.png")
        if self.directionRight == True:
            image(p1Right,self.x,self.y)
        elif self.directionRight == False:
            image(p1Left,self.x,self.y)
            
        
    def moveRight(self):
        self.x += 5
        self.directionRight = True
        
    def moveLeft(self):
        self.x -= 5
        self.directionRight = False
        
    def moveJump(self):
        self.x += 1
        
    
        

class Powerup:
    powerUpType = 0
    x = random(50,450)
    y = random(50,450)
    #powerUpType = 0
    type = 0
    
    def __init__(self,powerUpType,x):
        self.x = x
        self.y = 50
        self.powerUpType = powerUpType
        #self.powerUpType = int(random(3))
        if self.powerUpType == 0:
            self.powerUpImage = loadImage("defence.png")
            self.type = 0
        elif self.powerUpType == 1:
            self.powerUpImage = loadImage("attack.png")
            self.type = 1
        elif self.powerUpType == 2:
            self.powerUpImage = loadImage("health.png")
            self.type = 2

    #methods 
    def display(self):
            image(self.powerUpImage, self.x, self.y)
        
        

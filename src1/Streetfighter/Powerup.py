class Powerup:
    powerUpType = 0
    x = random(50,450)
    y = random(50,450)
    powerUpType = int(random(3))
    def __init__(self):
        self.x = 50
        self.y = 50
        self.powerUpType = int(random(3))

    #methods 
    def display(self):
        
        if self.powerUpType == 0:
            defence = loadImage("defence.png")
            image(defence, self.x, self.y)
        elif self.powerUpType == 1:
            attack = loadImage("attack.png")
            image(attack, self.x, self.y)
        elif self.powerUpType == 2:
            health = loadImage("health.png")
            image(health, self.x, self.y)
        
        

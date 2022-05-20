class Powerup:
    powerUpType = 0
    x = random(150,1350)
    y = random(150,700)
    def __init__(self):
        self.x = random(150,1350)
        self.y = random(150,700)

    #methods 
    def display(self):
        powerUpType = random(3)
        if powerUpType == 0:
            defence = loadImage("defence.png")
            image(defence, self.x, self.y)
        elif powerUpType == 1:
            attack = loadImage("attack.png")
            image(attack, self.x, self.y)
        elif powerUpType == 2:
            health = loadImage("health.png")
            image(health, self.x, self.y)

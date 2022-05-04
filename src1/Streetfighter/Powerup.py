class Powerup:
    powerUpType = 0
    x = random
    y = random
    def__init__(self):
        self.x = 0
        self.y = 0
    #methods 
    def display(self):
        powerUpType = random(3)
        if powerUpType == 0:
            defence = loadImage("defence.png")
            image(defence, 750, 500)
        elif powerUpType == 1:
            attack = loadImage("attack.png")
            Image(attack, 750, 500
        elif powerUpType == 2:
            health = loadImage("health.png")
            mage(health, 750, 500)

# from Arm import Arm
# from Platform import Platform
# from Player import Player
# from Powerup import Powerup
# from Shield import Shield
#from Startscreen import Startscreen
# c1 = Arm()
# c2 = Platform()
# c3 = Player()
# c4 = Powerup()
# c5 = Shield()

def setup():
    size(1500, 1000)
    background(110)
def draw():
    background(127)
    startScreen()

def startScreen():
    logo = loadImage("SpaceAssailents.png")
    background(40)
    fill(60)
    rect(100,100,1300,800)
    fill(255)
    textSize(72)
    textAlign(CENTER)
    text("Welcome to Space Assailant", 750,75)
    textSize(50)
    text("Press Space to start", 750,975)
    image(logo,750,500)

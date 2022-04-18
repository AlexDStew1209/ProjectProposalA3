# from Arm import Arm
# from Platform import Platform
# from Player import Player
# from Powerup import Powerup
# from Shield import Shield
# c1 = Arm()
# c2 = Platform()
# c3 = Player()
# c4 = Powerup()
# c5 = Shield()
screenLayer = 0

def setup():
    size(1500, 1000)
    background(151, 50, 201)

def draw():
    background(127)
    startScreen()

def startScreen():
    if screenLayer == 0:
        logo = loadImage("SpaceAssailents.png")
        background(40)
        fill(60)
        rect(100,100,1300,800)
        fill(255)
        textSize(72)
        textAlign(CENTER)
        text("Welcome to Space Assailant", 750,75)
        textSize(50)
        text("Press any key to start", 750,975)
        image(logo,750,500)
        if keyPressed == True:
            screenLayer = 1
        elif keyPressed == False:
            screenLayer = 0
            
    elif screenLayer == 1:
        text("Test",750,500)
        

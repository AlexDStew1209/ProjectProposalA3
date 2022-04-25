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
    global screenLayer
    background(127)
    if screenLayer == 0:
        startScreen()
    elif screenLayer == 1:
        instructScreen()
    elif screenLayer == 2:
        endScreen()

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
    text("Press S to start", 750,975)
    image(logo,750,500)
        
def instructScreen():
    text("test",750,500)
        
def keyPressed():
    global screenLayer
    # if key == CODED:
    #     if keyCode == UP:
    #         screenLayer = 1
    
    if key == ' ':
        screenLayer = 1
    if key == '1':
        screenLayer = 2
            

def endScreen():
    logo = loadImage("")
    background(40)
    fill (60)
    rect(250,25,1000,200)
    fill(255)
    textSize(170)
    textAlign(CENTER)
    text("Player x Wins!",750,175)
    fill(60)
    rect(200,250,1100,700)
    textAlign(CENTER)
    textSize(60)
    fill(255)
    text("Health: ",750,350)
    textSize(40)
    text("Thank you for playing Space Kerfuffle",750,500)
    text("By Alex Stewart, Jasper Mowdood and Stuart Pahnke ",750,550)
    textSize(70)
    text("To play again, press x",750,900)

# from Arm import *
# from Platform import *
# from Player import *
# from Powerup import *
# from Shield import *
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
        playScreen()
    elif screenLayer == 3:
        endScreen()
        
        
def playScreen():
    background1 = loadImage("BackgroundForSpaceKerfuffle.png")
    imageMode(CORNER)
    image(background1,100,100)

def startScreen():
    logo = loadImage("Logo.png")
    background(40)
    fill(60)
    rect(100,100,1300,800)
    fill(255)
    textSize(72)
    textAlign(CENTER)
    text("Welcome to Space Assailant", 750,75)
    textSize(50)
    text("Press space to start", 750,975)
    imageMode(CENTER)
    image(logo,750,500)
        
def instructScreen():
    background(40)
    fill(60)
    rect(100,100,1300,800)
    fill(255)
    textSize(56)
    textAlign(CENTER)
    text("Player 1: use WASD for movement, and F for punch", 750,200)
    text("Player 2: use IJKL for movement, and O for punch", 750,275)
    textSize(68)
    text("To Win:", 750,350)
    textSize(56)
    text("Push your opponent off the board:", 750,425)
    text("Or remove all their health", 750,500)
    textSize(68)
    text("Press space to continue", 750,600)
        
def keyPressed():
    global screenLayer
    if key == ' ':
        if screenLayer == 0:
            screenLayer = 1
        elif screenLayer == 1:
            screenLayer = 2
    if key == '1':
        screenLayer = 3
    if screenLayer == 2:
        if key == 'a':
            p1.moveLeft()
        elif key == 'd':
            p1.moveRight()
    
            

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

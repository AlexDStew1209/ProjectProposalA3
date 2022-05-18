# from Arm import *
# from Platform import *
from Player import *
# from Powerup import *
# from Shield import *
# c1 = Arm()
# c2 = Platform()
# c3 = Player()
# c4 = Powerup()
# c5 = Shield()
screenLayer = 0
winner = 0
roundNum = 1
p1 = Player(200,200,1)
p2 = Player(500,200,2)


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
    global screenLayer
    if p1.deaths == 3 or p2.deaths == 3:
        screenLayer = 3
    else:
        background(50)
        background1 = loadImage("BackgroundForSpaceKerfuffle.png")
        imageMode(CORNER)
        image(background1,100,100)
        p1.display()
        p2.display()
        rectMode(CORNER)
        fill(255,0,0)
        rect(100,850,1300,50)
        scoreboard()
        gameOverLogic()


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
        elif key == 'j':
            p2.moveLeft()
        elif key == 'l':
            p2.moveRight()
        elif key == 'w':
            p1.moveUp()
        elif key == 'i':
            p2.moveUp()
        elif key == 'f':
            p1.attack()
            player1PlayerAttackDetection()
        elif key == 'h':
            p2.attack()
            player2PlayerAttackDetection()

def player1PlayerAttackDetection():
    if dist(p1.x,p1.y,p2.x,p2.y) < 43:
        p2.health = (p2.health - p1.damage)
        
        
def player2PlayerAttackDetection():
    if dist(p1.x,p1.y,p2.x,p2.y) < 43:
        p1.health = (p1.health - p2.damage)
        
def endScreen():
    global winner
    logo = loadImage("Logo.png")
    if p1. deaths == 3:
        winner = 2
    elif p2.deaths == 3:
        winner = 1
    background(40)
    fill (60)
    rect(250,25,1000,200)
    fill(255)
    textSize(170)
    textAlign(CENTER)
    text("Player    Wins!",750,175)
    text(winner,775,175)
    fill(60)
    rect(200,250,1100,700)
    textAlign(CENTER)
    textSize(60)
    fill(255)
    text("Won 3 out of     rounds ",750,350)
    text(roundNum,815,350)
    textSize(40)
    text("Thank you for playing Space Kerfuffle",750,500)
    text("By Alex Stewart, Jasper Mowdood and Stuart Pahnke ",750,550)
    textSize(70)
    text("To play again, press x",750,900)
    imageMode(CENTER)
    image(logo,750,700,250,250)
    
def scoreboard():
    textSize(50)
    textAlign(CENTER)
    rectMode(CORNER)
    fill(100)
    stroke(255,0,0)
    strokeWeight(4)
    rect(40,10,200,75)
    fill(0)
    text("Round: ",125,60)
    text(roundNum, 220,60)
    text(p1.health,500,50)
    text(p2.health,600,50)
    text(p1.deaths,700,50)
    text(p2.deaths,800,50)
    strokeWeight(1)
    
    
def gameOverLogic():
    global roundNum
    if p1.health <= 0:
        p1.deaths += 1
        roundNum += 1
        p1.health = 100
        p2.health = 100
        p1.x = 200
        p1.y =200
        p2.x = 500
        p2.y =200
    if p2.health <= 0:
        p2.deaths += 1
        roundNum += 1
        p1.health = 100
        p2.health = 100
        p1.x = 200
        p1.y = 200
        p2.x = 500
        p2.y = 200
    

# from Platform import *
from Player import *
from Powerup import *
# c2 = Platform()
# c4 = Powerup()
screenLayer = 0
winner = 0
roundNum = 1
p1 = Player(300,650,1)
p2 = Player(1000,650,2)
worldy = 1000
worldx = 1500
pu1 = Powerup(1,50)
pu2 = Powerup(2,75)
pu3 = Powerup(3,100)
pu4 = Powerup(1,125)


def setup():
    size(worldx, worldy)
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
        powerUp = Powerup(1,800)
        powerUp.display()
        #powerUpLogic()
        p1.down()
        p2.down()
        borderDetection()
        
def powerUpLogic():
        # if p1.health <= 50:
    #     pu1.x = int(random(150,1350))
    # if p2.health <= 50:
    #     pu2.x = int(random(150,1350))
    # if p1.health <= 25:
    #     pu3.x = int(random(150,1350))
    # if p2.health <= 25:
    #     pu4.x = int(random(150,1350))
    pu1.display()
    pu2.display()
    pu3.display()
    pu4.display()
    #pu1
    # if dist(p1.x,p1.y,pu1.x,pu1.y) < 25:
    #     if pu1.type == 0:
    #         p2.damage = p2.damage/2
    #     elif pu1.type == 1:
    #         p1.damage = p1.damage * 2
    #     elif pu1.type == 2:
    #         p1.health += 25
    # if dist(p2.x,p2.y,pu1.x,pu1.y) < 25:
    #     if pu1.type == 0:
    #         p1.damage = p1.damage/2
    #     elif pu1.type == 1:
    #         p2.damage = p2.damage * 2
    #     elif pu1.type == 2:
    #         p2.health += 25
    #pu2

def startScreen():
    logo = loadImage("Logo.png")
    background(40)
    fill(60)
    rect(100,100,1300,800)
    fill(255)
    textSize(72)
    textAlign(CENTER)
    text("Welcome to Pixel Fighter", 750,75)
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
    #text("Push your opponent off the board:", 750,425)
    text("Remove all of your opponents health", 750,500)
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
            
def borderDetection():
    if p1.y > (700):
        p1.y = 700
    if p2.y > (700):
        p2.y = 700
    if p1.x > (1275):
        p1.x = 1275
    if p2.x > (1275):
        p2.x = 1275
    if p1.x < (28):
        p1.x = 28
    if p2.x < (28):
        p2.x = 28
    if p1.y < (90):
        p1.y = 90
    if p2.y < (90):
        p2.y = 90


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
    text(roundNum - 1,815,350)
    textSize(40)
    text("Thank you for playing Pixel Fighter",750,500)
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
    #Player 1 Stats
    fill(100)
    stroke(255,0,0)
    strokeWeight(4)
    rect(400,10,400,75)
    fill(0)
    textSize(55)
    text("Player 1:",500,60)
    textSize(30)
    text("Health:", 675,40)
    text(p1.health,750,40)
    text("Deaths:", 675,70)
    text(p1.deaths,750,70)
    #Player 2 Stats
    fill(100)
    stroke(255,0,0)
    strokeWeight(4)
    rect(900,10,400,75)
    fill(0)
    textSize(55)
    text("Player 2:",1000,60)
    textSize(30)
    text("Health:", 1175,40)
    text(p2.health,1250,40)
    text("Deaths:", 1175,70)
    text(p2.deaths,1250,70)
    strokeWeight(1)
    
    
def gameOverLogic():
    global roundNum
    if p1.health <= 0:
        p1.deaths += 1
        roundNum += 1
        p1.health = 100
        p2.health = 100
        p1.x = 300
        p1.y = 650
        p2.x = 1000
        p2.y = 650
    if p2.health <= 0:
        p2.deaths += 1
        roundNum += 1
        p1.health = 100
        p2.health = 100
        p1.x = 300
        p1.y = 650
        p2.x = 1000
        p2.y = 650
    

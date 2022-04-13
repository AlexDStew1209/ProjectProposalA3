class Startscreen:
    #Member Variables
    screen = 0
    
    #Constructor
    def __init__(self):
        self.screen = 0
        
    #Methods
    def display(self):
        startScreen()
        
        
    def startScreen(self):
        if screen == 0:
            background(40)
            textSize(72)
            textAlign(CENTER)
            text("Welcome to Space Assailant", 750,500)
        
        

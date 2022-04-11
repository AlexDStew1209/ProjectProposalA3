class Arm:
    #Member Variables
    reach = 10
    armColor = 0
    damage = 10
    #Constructor
    def __init__(self,armColor):
        
        self.armColor = armColor
    #Methods
    def display(self):
        fill(self.armColor)
        rect(x,y,25,50)
        

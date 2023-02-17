
from graphics import *
import random
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DEFAULT_FISH_NUM = 10
DEFAULT_BUBBLE_NUM = 25

#---------
# FISH CLASS
#---------


class Fish:
    def __init__(self, x, y, color, speed):
        self.count = 0
        self.speed = speed
        self.color = color
        self.body = Oval(Point(x, y), Point(x+60, y+40))
        if speed > 0:
            self.eyes = Circle(Point(x+45, y+15), 3)
            center_x = ((x+x+60)/2)-20
            center_y = (y+y+40)/2
            self.tail = Oval(Point(center_x, center_y+30), Point(center_x+10, center_y-30))
        elif self.speed < 0:
            self.eyes = Circle(Point(x+20, y+15), 3)
            center_x = ((x+x+60)/2)+20
            center_y = (y+y+40)/2
            self.tail = Oval(Point(center_x, center_y+30), Point(center_x-10, center_y-30))

    def draw(self, window):

        self.body.setFill(self.color)
        self.body.draw(window)
        self.eyes.draw(window)
        self.tail.draw(window)
        self.eyes.setFill("white")
        self.body.setFill(self.color)
        self.body.setOutline(self.color)
        self.tail.setOutline(self.color)
        self.tail.setFill(self.color)

    def move(self):
        p1 = self.body.getP1()
        p2 = self.body.getP2()
        total = (p1.getX() / 2) + (p2.getX() / 2)
        if self.count > 20:
            self.count = 0
        if self.speed > 0:
            if total > 810:
                self.body.move(-WINDOW_WIDTH, 0)
                self.tail.move(-WINDOW_WIDTH, 0)
                self.eyes.move(-WINDOW_WIDTH, 0)
            elif total <= 810:
                if self.count < 10:
                    self.body.move(self.speed, -1)
                    self.tail.move(self.speed, -1)
                    self.eyes.move(self.speed, -1)
                elif self.count >= 10:
                    self.body.move(self.speed, 1)
                    self.tail.move(self.speed, 1)
                    self.eyes.move(self.speed, 1)
        elif self.speed < 0:
            if total > -1:
                if self.count < 10:
                    self.body.move(self.speed, -1)
                    self.tail.move(self.speed, -1)
                    self.eyes.move(self.speed, -1)
                elif self.count >= 10:
                    self.body.move(self.speed, 1)
                    self.tail.move(self.speed, 1)
                    self.eyes.move(self.speed, 1)
            if total <= -1:
                self.body.move(WINDOW_WIDTH, 0)
                self.tail.move(WINDOW_WIDTH, 0)
                self.eyes.move(WINDOW_WIDTH, 0)
        self.count +=1





#---------
# BUBBLE CLASS
#---------

class Bubble:
    def __init__(self, x, y, speed):

        self.circle = Circle(Point(x, y), 5)
        self.speed = speed
        self.count = 0

    def draw(self, window):
        self.circle.setFill("white")
        self.circle.draw(window)

    def move(self):
        p1 = self.circle.getP1()
        p2 = self.circle.getP2()
        total = (p1.getY()/2) + (p2.getY()/2)
        if self.count > 20:
            self.count = 0
        if total >= -1:
            if self.count >= 10:
                self.circle.move(1, self.speed)
            elif self.count < 10:
                self.circle.move(-1, self.speed)
        elif total < -1:
            self.circle.move(0, WINDOW_HEIGHT-20)
        self.count += 1





#------------------
# HELPER FUNCTIONS
#------------------

def setUpInput(win, point, text):
    '''
    creates an Entry box with a label
    
    Params:
    win (GraphWin): the window the Entry box and label with be drawn in.
    point (Point): the location od the center of the text label
    text (str): the words that will be used to label the Entry box
    
    Returns:
    the Entry object created
    '''
    winText = Text(point, text)
    winText.setSize(18)
    winText.draw(win)
    winBox = Entry(Point(point.getX() + 225, point.getY()), 5)
    winBox.setSize(18)
    winBox.draw(win)
    return winBox

def getInput(win):
    '''
    Allows the user to enter the number of fish and bubbles for the aquarium.
    If a value is not entered or an invalid value (like a letter) is entered,
    the default number is used for that value.
    
    Params:
    win (GraphWin): the window the Entry box is in
    
    Returns:
    the number of fish and number of bubbles that will be drawn in the aquarium
    as a tuple
    '''
    directions = Text(Point(WINDOW_WIDTH/2 , 400), 'Enter the number of fish and bubbles, then click in the window.')
    directions.draw(win)
    fishEntry = setUpInput(win, Point(300, 200), "Enter number of fish:")
    bubbleEntry = setUpInput(win, Point(300, 300), "Enter number of bubbles:")
    win.getMouse()
    if fishEntry.getText().isdigit() and int(fishEntry.getText()) >= 0:
        numFish = int(fishEntry.getText())
    else:
        numFish = DEFAULT_FISH_NUM
    if bubbleEntry.getText().isdigit() and int(bubbleEntry.getText()) >= 0:
        numBubbles = int(bubbleEntry.getText())
    else:
        numBubbles = DEFAULT_BUBBLE_NUM
    fishEntry.undraw()
    bubbleEntry.undraw()
    directions.undraw()
    cover = Rectangle(Point(0, 0), Point(WINDOW_WIDTH, WINDOW_HEIGHT))
    cover.setFill("cyan")
    cover.draw(win)
    return numFish, numBubbles

def randColor():
    '''
    Returns a random color created from randomly generated red, green, and blue values
    '''
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return color_rgb(red, green, blue)


def setupFish(numFish):
    '''
    Creates the list of fish with random position, color and speed
    
    Params:
    numFish (int): the number of fish to be added to the list
    
    Returns:
    the list of fish
    '''
    fish = []
    for _ in range(numFish):
        random_x = random.randint(80, WINDOW_WIDTH-80)
        random_y = random.randint(60, WINDOW_HEIGHT-60)
        x = 0
        while x == 0:
            random_speed = random.randint(-5, 5)
            x += random_speed

        fish.append([(random_x, random_y), random_speed])
    return fish


def setupBubbles(numBubbles):
    '''
    Creates the list of bubbles with random position and speed

    Params:
    numBubbles (int): the number of bubbles to be added to the list
    
    Returns:
    the list of bubbbles
    '''
    bubbles = []
    for _ in range(numBubbles):
        random_x = random.randint(10, WINDOW_WIDTH-10)
        random_y = random.randint(10, WINDOW_HEIGHT-10)

        random_speed = random.randint(-5, -1)
        bubbles.append([(random_x, random_y), random_speed])
    return bubbles


#------
# MAIN
#------
def main():

    # make the graphics window (use autoflush=False to update more frequently)
    # makes the animation move more smoothly
    win = GraphWin("Swimming Fish", WINDOW_WIDTH, WINDOW_HEIGHT, autoflush=False)
    win.setBackground("cyan2")
    
    numFish, numBubbles = getInput(win)
                      
    # call helper functions to setup the fish and bubble lists
    bubbles = setupBubbles(numBubbles)
    bubbles_list = []
    for bubble in bubbles:
        cor_x = bubble[0][0]
        cor_y = bubble[0][1]
        speed = bubble[1]

        # draw the fish and bubbles in their initial locations
        bubble = Bubble(cor_x, cor_y, speed)
        bubbles_list.append(bubble)
        bubble.draw(win)

    fishes = setupFish(numFish)
    fish_list = []
    for fish in fishes:
        cor_x = fish[0][0]
        cor_y = fish[0][1]
        color = randColor()
        speed = fish[1]
        # draw the fish and bubbles in their initial locations
        fish = Fish(cor_x, cor_y, color, speed)
        fish_list.append(fish)
        fish.draw(win)


        
    # continue swimming until the user clicks
    keepSwimming = True
    
    while keepSwimming:
        # loop through all the fish, moving each a little bit
        for fish in fish_list:
            fish.move()

        # loop through all the bubbles, moving each a little bit
        for bub in bubbles_list:
                bub.move()


        # The bubble are after the fish so that the bubbles are drawn in front of the fish

        
        update(50) # call update to flush the window
        # if user clicks: stop swimming
        if win.checkMouse() != None:
            keepSwimming = False

    win.close()

if __name__ == '__main__':
    main()


from graphics import *
from math import *

def main():
    w = GraphWin("Target Practice",400,400)
    w.setCoords(-250,-250,250,250)

    origin = Point(0,0)

    for radius in range(10,0,-1):
        c = Circle(origin, 20*radius)

        if radius % 2 == 0:
            c.setFill("Red")
        else:
            c.setFill("Yellow")
        
        c.draw(w)

    #draw message after drawing the target
    t = tMessage(w)
    gamePlaying(w,origin,t)
    w.getMouse()
    w.close()

def dist(p1,p2):
    dist = sqrt((p1.getX()-p2.getX())**2 + (p1.getY() - p2.getY())**2)

    return dist

def tMessage(w):

    t = Text(Point(0,-225) , "Click on the target")
    t.setSize(20)
    t.draw(w)
    return t

def gamePlaying(w,origin,t):

    p = w.getMouse()
    d = dist(origin,p)

    if d < 20:
        t.setText("Bullseye!")
    if d > 20:
        t.setText("Missed!")
    
main()

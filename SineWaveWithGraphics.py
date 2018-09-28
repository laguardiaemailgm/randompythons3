
from math import *
from graphics import *
from time import *

def goodSine():
    veloc = .5  #horizontal velocity (pixels per second)
    amp = 50    #sine wave amplitude (pixels)
    freq = .01  #oscillations per second

    #Set up a graphics window:
    win = GraphWin("Good Sine Waves",800,600)
    win.setCoords(0.0, -100.0, 200.0, 100.0)

    #Draw a line for the x-axis:
    p1 = Point(0,0)
    p2 = Point(200,0)
    xAxis = Line(p1,p2)
    xAxis.draw(win)

    #Draw a ball that follows a sine wave
    for time in range(1000):
        x = time*veloc
        #y = amp*sin(freq*time*2*pi) to make it bounce use abs()
        y = abs(amp*sin(freq*time*2*pi))
        ball = Circle(Point(x,y),2)
        ball.draw(win)
        sleep(0.1)  #Needed so that animation runs slowly enough to be seen


    win.getMouse()
    win.close()
    
goodSine()

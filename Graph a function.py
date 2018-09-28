from graphics import *
from math import *

def main():
    print("This program will graph a function...")
    
    function, left, right, top, bottom = getUserData()

    win = setUpWindow(left, right, top, bottom, function)
    drawGraph(win, function, left, right)

    win.getMouse()
    win.close()

def getUserData():
    print("This program graphs an arbitrary math function.")
    print("You must enter the x and y ranges to be displayed.")
    left = eval(input("Enter x coordinate for left edge of window: "))
    right = eval(input("Enter x coordinate for right edge of window: "))
    bottom = eval(input("Enter y coordinate for lower edge of window: "))
    top = eval(input("Enter y coordinate for upper edge of window: "))
    function = input("Enter function expression to be graphed, with x as variable: ")
    return function, left, right, top, bottom

def setUpWindow(left, right, top, bottom, function):
    win = GraphWin("Graph of " + function, 500, 500)
    win.setCoords(left, bottom, right, top)
    Line(Point(left, 0), Point(right, 0)).draw(win)
    Line(Point(0, bottom), Point(0, top)).draw(win)
    return win

def drawGraph(win, function, left, right):
    increment = (right-left)/100
    x = left
    rightPoint = Point(x, eval(function))
    for n in range(100):
        leftPoint = rightPoint
        x += increment
        rightPoint = Point(x, eval(function))
        Line(leftPoint, rightPoint).draw(win)
main()

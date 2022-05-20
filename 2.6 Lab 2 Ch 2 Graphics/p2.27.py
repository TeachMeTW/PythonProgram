from tkinter import Canvas
import ezgraphics

def initBuilding(canvas):
    # building
    canvas.setFill("gray")
    canvas.drawRect(100, 1000, 500, -600)

    # Side wall
    canvas.drawPolygon(600, 1000, 600, 400, 800, 300, 800, 900)

    # Roof
    canvas.drawPolygon(100, 400, 300, 300, 600, 300, 800, 300)
    canvas.drawPolygon(100, 400, 800, 300, 600, 400)

    # door
    canvas.setFill("brown")
    canvas.drawRect(150, 1000, 50, -75)

    # door knob
    canvas.setFill("yellow")
    canvas.drawOval(155, 960, 10, 10)

def initWindows(canvas):
    # windows
    xBorderL = 120
    yBorderT = 420
    totalWindowsX = 8                   # change this for number of windows in x Direction
    totalWindowsY = 12                  # change this for number of windows in y Direction
    winHeight = 30
    winWidth = 48
    winSpacing = 10

    canvas.setFill(210, 180, 140)       # color of windows

    for x in range(totalWindowsX): # Generate windows in X direction

        #update window positon

        winPositionX = xBorderL + (winSpacing * x) + (winWidth * x)     
        winPositionY = yBorderT + winSpacing                           

        canvas.drawRect(winPositionX, winPositionY, winWidth, winHeight)

        for y in range(totalWindowsY): # Generate all windows in Y direction
            canvas.drawRect(winPositionX, winPositionY + (winHeight * y + winSpacing * y), winWidth, winHeight)
        
    # Side windows
    # Such a crude way to do it
    canvas.setFill(210, 180, 110)
    # Spacing between
    mult = 50
    # Slanted window
    canvas.drawPoly(620,900, 620, 870, 650, 850, 650, 880)
    for x in range(10):
        # From what I notice, the spacing is X times along x axis and X/2 times along y axis
        canvas.drawPoly(620,900-(mult*x), 620, 870-(mult*x), 650, 850-(mult*x), 650, 880-(mult*x))
        canvas.drawPoly(620+mult,900-(mult*x+mult/2), 620+mult, 870-(mult*x+mult/2), 650+mult, 850-(mult*x+mult/2), 650+mult, 880-(mult*x+mult/2))
        canvas.drawPoly(620+(2*mult),900-(mult*x+mult), 620+(2*mult), 870-(mult*x+mult), 650+(2*mult), 850-(mult*x+mult), 650+(2*mult), 880-(mult*x+mult))
        canvas.drawPoly(620+(3*mult),900-(mult*x+mult*1.5), 620+(3*mult), 870-(mult*x+mult*1.5), 650+(3*mult), 850-(mult*x+mult*1.5), 650+(3*mult), 880-(mult*x+mult*1.5))

def main():
    win = ezgraphics.GraphicsWindow(2000, 1000)
    win.setTitle("Graphics P2.25")
    canvas = win.canvas()
    initBuilding(canvas)
    initWindows(canvas)
    win.wait() 
    
main()
import ezgraphics

# basic smiley face

def main():
    # Initialize the graphics window
    win = ezgraphics.GraphicsWindow(1000, 1000)
    win.setTitle("Graphics P2.25")

    # Set the canvas black because why not? 
    canvas = win.canvas()
    canvas.setBackground("black")

    # Since we are drawing on a black canvas, I set color to white
    canvas.setOutline("white")
    xOff = 300
    yOff = 300
    canvas.drawOval(xOff,yOff, 200,200)

    # this would be the eye whites
    canvas.setFill("white")
    canvas.drawOval(xOff+40,yOff+50, 200/4,200/4)
    canvas.drawOval(xOff+110,yOff+50, 200/4,200/4)

    # Black middle of the eye (can be changed to a diff color)
    canvas.setFill("black")
    canvas.drawOval(xOff+50,yOff+60, 200/8,200/8)
    canvas.drawOval(xOff+120,yOff+60, 200/8,200/8)

    # The semi smile
    canvas.setFill("white")
    canvas.drawOval(xOff+40, yOff+120, 120, 30)

    # To cover up the top of the smile (to half the oval)
    canvas.setFill("black")
    canvas.setOutline("black")
    canvas.drawRectangle(xOff+40,yOff+105, 120, 30)
    
    win.wait()
    
main()
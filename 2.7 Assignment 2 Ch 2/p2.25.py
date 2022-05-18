import ezgraphics

# basic smiley face

win = ezgraphics.GraphicsWindow(1000, 1000)
win.setTitle("Graphics P2.25")

canvas = win.canvas()
canvas.setBackground("black")

canvas.setOutline("white")
xOff = 300
yOff = 300
canvas.drawOval(xOff,yOff, 200,200)

canvas.setFill("white")
canvas.drawOval(xOff+40,yOff+50, 200/4,200/4)
canvas.drawOval(xOff+110,yOff+50, 200/4,200/4)

canvas.setFill("black")
canvas.drawOval(xOff+50,yOff+60, 200/8,200/8)
canvas.drawOval(xOff+120,yOff+60, 200/8,200/8)

canvas.setFill("white")
canvas.drawOval(xOff+40, yOff+120, 120, 30)

canvas.setFill("black")
canvas.setOutline("black")
canvas.drawRectangle(xOff+40,yOff+105, 120, 30)


win.wait()
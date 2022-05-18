import ezgraphics

win = ezgraphics.GraphicsWindow(1000, 1000)
win.setTitle("P2.31")
canvas = win.canvas()



# Draw several bars.
canvas.setFill("red")
canvas.drawRectangle(100, 490, 420, 50)
canvas.drawText(105, 500, "Golden Gate Bridge: 4,200 ft " )
canvas.setFill("gray")
canvas.drawRectangle(100, 420, 159.5, 50)
canvas.drawText(105, 430, "Brooklyn Bridge: 1,595 ft " )
canvas.setFill("white")
canvas.drawRectangle(100, 350, 215, 50)
canvas.drawText(105, 360, "Delaware Memorial Bridge: 2,150 ft " )
canvas.setFill("blue")
canvas.drawRectangle(100, 280, 380, 50)
canvas.drawText(105, 290, "Mackinac Bridge: 3,800 ft " )
canvas.setFill("yellow")
canvas.drawRectangle(100, 210, 700, 50)
canvas.drawText(105, 220, "How fat I am: 7,000 ft " )

# Draw the axes with tick marks.
canvas.drawLine(100, 550, 100, 100)
canvas.drawArrow(100, 550, 900, 550)
canvas.drawText(910, 550, "ft")

xOffset = 100
for i in range(15) :
  canvas.drawLine(xOffset, 560, xOffset, 550)
  xOffset = xOffset + 100

canvas.drawText(100, 590, "(Bridge Length in Feet) \nEach mark is 1000 feet" )

# Wait for the user to close the window.
win.wait()
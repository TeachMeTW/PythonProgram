import ezgraphics



def initData(canvas):
  # Draw rectangles based on data provided. However this would be on a scale 10x less to fit.
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
  canvas.drawText(105, 300, "Mackinac Bridge: 3,800 ft " )
  canvas.setFill("yellow")
  canvas.drawRectangle(100, 210, 700, 50)
  canvas.drawText(105, 230, "How fat I am: 7,000 ft " )


def initGraph(canvas):
  # Draw the axes with tick marks.
  canvas.drawLine(100, 550, 100, 180)
  canvas.drawArrow(100, 550, 900, 550)

  canvas.drawText(905, 530, "(Bridge Length) \n    (in Feet)")
  canvas.drawText(100, 160, "(Bridges)")

  xOffset = 100
  for i in range(9) :
    canvas.drawLine(xOffset, 560, xOffset, 550)
    canvas.drawText(xOffset-10,570, str((xOffset*10)-1000) + " ft")
    xOffset = xOffset + 100

def main():
  win = ezgraphics.GraphicsWindow(1000, 1000)
  win.setTitle("P2.31")
  canvas = win.canvas()  
  initData(canvas) 
  initGraph(canvas)
  win.wait()
# Wait for the user to close the window.
main()
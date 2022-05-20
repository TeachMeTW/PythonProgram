import ezgraphics


def main():
    
    # Init graphics window
    win = ezgraphics.GraphicsWindow(1000, 1000)
    win.setTitle("Graphics P2.30")
    canvas = win.canvas()
    # changed to black because white is harder on the eyes
    canvas.setBackground("Black")
    
    # Blue ring
    canvas.setOutline("Blue")
    # can be changed depending on how thicc you want the rings
    canvas.setLineWidth(15)
    canvas.drawOval(100, 300, 200, 200)

    # Purple ring
    canvas.setOutline("Purple")
    # can be changed depending on how thicc you want the rings
    canvas.setLineWidth(15)
    canvas.drawOval(320, 300, 200, 200)
  
    # Red ring
    canvas.setOutline("Red")
    # can be changed depending on how thicc you want the rings
    canvas.setLineWidth(15)
    canvas.drawOval(540, 300, 200, 200)
   
    # Yellow ring
    canvas.setOutline("Yellow")
    # can be changed depending on how thicc you want the rings
    canvas.setLineWidth(15)
    canvas.drawOval(200, 400, 200, 200)
   
    # Green ring
    canvas.setOutline("Green")
    # can be changed depending on how thicc you want the rings
    canvas.setLineWidth(15)
    canvas.drawOval(420, 400, 200, 200)

    
    win.wait()
    
main()
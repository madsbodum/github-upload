from ball import ball
ddy = 0.3
b = ball()

def setup():
    size(1000,1000)
    
def draw():
    global b, ddy
    background(0)
    b.render()
    b.update(ddy)
    
def mousePressed():
    global b
    if b.mouseWithinBall():
        b.caught = True
        
def mouseReleased():
    global b
    if b.caught:
        b.dx = mouseX - pmouseX
        b.dy = mouseY - pmouseY
        b.caught = False

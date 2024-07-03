#存檔p04_mousePressed_line_mouseX_mouseY
def setup ():
    size(500,500)
    background(154,31,237)
def draw():
    if mousePressed:
        line(mouseX,mouseY,pmouseX,pmouseY)    

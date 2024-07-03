#P11_for_many_image
def setup ():
    global imgBG,img01
    size(675,1200)#用你的background.jpg圖的大小
    imgBG=loadImage("background.jpg")
    img01=loadImage("img01.png")#找半透明的圖
def draw():
    global imgBG,img01
    image(imgBG,0,0)
    for i in range (10):
        image(img01,i*100,0,350,300)
    image(img01,mouseX,mouseY,350,300)
    

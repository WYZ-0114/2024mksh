#P12_for_many_image_list_def_mousePreaaed
def setup ():
    global imgBG,img01
    size(675,1200)#用你的background.jpg圖的大小
    imgBG=loadImage("background.jpg")
    img01=loadImage("img01.png")#找半透明的圖
def draw():
    global imgBG,img01
    image(imgBG,0,0)
    for i in range (10):
        image(img01,x[i],y[i],350,300)
    image(img01,mouseX,mouseY,350,300)
x=[0]*10
y=[0]*10
N=0
def mousePressed():
    global N
    x[N],y[N]=mouseX,mouseY
    N +=1
    

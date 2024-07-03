#P13_for_list_append
def setup ():
    global imgBG,img01
    size(675,1200)#用你的background.jpg圖的大小
    imgBG=loadImage("background.jpg")
    img01=loadImage("img01.png")#找半透明的圖
def draw():
    global imgBG,img01
    image(imgBG,0,0)
    for i in range (len(x)):
        image(img01,x[i],y[i],350,300)
    image(img01,mouseX,mouseY,350,300)
x=[]#x=[0]*10
y=[]#y=[0]*10
#N=0
def mousePressed():
    x.append(mouseX)#global N
    y.append(mouseY)#x[N],y[N]=mouseX,mouseY
    #N +=1
    

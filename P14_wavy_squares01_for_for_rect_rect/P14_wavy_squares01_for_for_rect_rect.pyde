#P14_wavy_squares01_for_for_rect_rect
size(480,480)
for i in range(16):
    for j in range(16):
        rect(i*30,j*30,30,30)
        rect(i*30+2,j*30+2,9,9)
        rect(i*30+18,j*30+18,9,9)

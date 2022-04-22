myColorList = [
    (1, 0, 0), # red
    (1, .65, 0), # orange
    (1, 1, 0), # yellow
    (0, 1, 0), # green
    (93/255, 208/255, 1), # blue
    (50/255, 60/255, 190/255), # indigo
    (238/255, 130/255, 238/255), # violet,
    ]
# removed white (1,1,1) from the list

# draw each frame
for frame in range(7):
    newPage(1000,500)
    frameDuration(1)
    fill(1,1,1)    
    rect(0,0,1000,500)
    xx = 0 # origin x 
    yy = -height() # origin y 
    wide = width() # starting width
    high = 2*height() # starting height
    zz = 0 # increment
    col = 0 # starting color
    #draw new rainbow
    for stripe in range(7):
        myColor = myColorList[col]
        fill(*myColor)
        oval(xx+zz, yy+zz, wide-(2*zz), high-(2*zz)) 
        col += 1
        zz += 50
    # draw inner white circle
    fill(1,1,1)
    oval(350, -150, 300, 300)
    #move color from 0 position to end of list
    swap = myColorList[0]
    myColorList.pop(0)
    myColorList.append(swap)
    
# saveImage('rainbow.gif')
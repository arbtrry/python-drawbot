# setup
size = 150
# colors
blk = (0,)
dkgy = (.25,)
ltgy = (.75,)
yllw = (1,1,.5)

def socks():
    # rectangles
    fill(*dkgy)
    rect(0,0,size,size)
    rect(size,size,size,size)
    fill(*blk)
    rect(size,0,size,size)
    fill(*ltgy)
    rect(0,size,size,size)
    # lines
    stroke(*yllw)
    strokeWidth(size/50)
    line((size/2,0),(size/2,2*size))
    line((size*3/2,0),(size*3/2,2*size))
    line((0,size/2),(2*size,size/2))
    line((0,size*3/2),(2*size,size*3/2))
    # clearout lines
    stroke(None)

# flatten pattern
scale(1.33,1)
# make argyle out of grid
rotate(45)
# pull origin off canvas
translate(-444,-544)

# give it height by repeating row
for every in range(8):
    # row-making
    for each in range(8):
        socks()
        translate(2*size,0)
    translate(-16*size,2*size)

# saveImage('socks.png')
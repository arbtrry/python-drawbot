# pattern based on Maldon sea salt flakes box
# draw the basic pattern box
def maldon():
    fill(.1,.45,.2) # bright green
    rect(0,0,250,250)
    fill(.81,.92,.84) # pale mint green
    rect(50,50,200,200)
    fill(.12,.2,.12) # dark green gray
    rect(100,100,100,100)

# create page, give it background, 
# pull origin off canvas, and rotate
newPage(1000,1000)
fill(.1,.45,.2)
rect(0,0,1000,1000)
translate(500,-500)   
rotate(45)

# repeat rows up
for every in range(8):
    # draw row of pattern boxes
    for each in range(8):
        maldon()
        translate(250,0)
    translate(-2000,250)
    
# saveImage('maldon-box.png')
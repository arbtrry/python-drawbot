size('Letter')

# Set up variables
inch=72
margin=.25*inch
diam=1.4375*inch
block=diam+margin

# Determine how many labels on a page
countAcross=floor(width()//block)
countUp=floor(height()//block)

# print(diam, ' is the diameter of each label')
# print(block, ' is the height and width per block')
# print(countAcross, ' labels across')
# print(countUp, ' labels high')
# print('thus ',countAcross*countUp,' labels per letter page')

# Fill a page with solid fake labels?
for every in range(countUp):
    for each in range(countAcross):
        fill(146/255, 199/255, 145/255)
        oval(margin, margin, diam, diam)
        translate(block,0)
    translate(-block*countAcross,block)
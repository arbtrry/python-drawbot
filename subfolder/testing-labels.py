size('Letter')
import random

# Set up variables
inch=72
margin=.25*inch
diam=1.4375*inch
block=diam+margin

# Determine how many labels on a page
countAcross=floor(width()//block)
countUp=floor(height()//block)

# print('thus ',countAcross*countUp,' labels per letter page')

# Color options
fillColorList = [(.57, .78, .57),  (.57, .72, .96), (.84, .84, .57), (.78, .55, .78)]
strokeColorList = [(.57, .57, .57), (.75, .5, .5), (.64, .9, .9), (.75, .75, .64)]

# Defaults
fill(.57, .78, .57)
stroke(.57, .57, .57)
strokeWidth(4)

# Fill a page with fake labels?
for every in range(countUp):
    for each in range(countAcross):
        stroke(*random.choice(strokeColorList)) 
        fill(*random.choice(fillColorList))
        oval(margin, margin, diam, diam)
        translate(block,0)
    translate(-block*countAcross,block)
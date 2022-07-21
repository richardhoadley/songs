# expressive materials
# percussion and melody instrument

import math
import random
import time

#from helpers import render_example

from neoscore.core import neoscore
from neoscore.core.paper import Paper
from neoscore.core.brush import Brush
from neoscore.core.color import Color
from neoscore.core.path import Path
from neoscore.core.pen import Pen
from neoscore.core.point import ORIGIN, Point
from neoscore.core.positioned_object import PositionedObject
from neoscore.core.text import Text
from neoscore.core.rich_text import RichText
from neoscore.core.units import ZERO, Mm

from functions import stones, oneEllipse, manyEllipses
from haiku import haiku

#neoscore.setup()
neoscore.setup(paper=Paper(Mm(297), Mm(210), Mm(10), Mm(10), Mm(10), Mm(10)))


#cd '/Users/rich/Documents/music/neoscore/neoscore-main/expressive_materials/' && '/usr/local/bin/python3'  '/Users/rich/Documents/music/neoscore/neoscore-main/expressive_materials/em002.py'

pageNum = 0


random.seed()
randColour = random.random()
randSizeFactor = random.random()



title = Text((Mm(100), Mm(0)), None, "Expressive Materials")






# num, length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation
# manyEllipses(5, neoscore.document.pages[0], 5, 5, 30, 0, 0, 0, 360)


# the cursor
l1 = Path.straight_line(
                        (Mm(0), Mm(0)),
                        None,
                        (Mm(0), Mm(190)),
                        None,
                        Brush(Color(255, 255, 0, int(40*randColour))),
                        Pen(color="#ff0000", thickness=Mm(0.5)),
                        )




# xPos, yPos, parent, width, height, rotation
#oneEllipse(10, 10, neoscore.document.pages[0], 3, 3, 360)
#oneEllipse(15, 10, neoscore.document.pages[0], 3, 3, 360)
#oneEllipse(20, 10, neoscore.document.pages[0], 3, 3, 360)
#oneEllipse(25, 10, neoscore.document.pages[0], 3, 3, 360)
#oneEllipse(30, 10, neoscore.document.pages[0], 3, 3, 360)




# num, parent, length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation
manyEllipses(10, pageNum, 4, 4, 20, 0, 10, 10, 360)


#stones function is in functions.py
# num, xPos, yPos
stones(10, 80, 10)

stones(10, 120, 10)


haikuText = haiku()
#text = Text((Mm(50), Mm(-10)), None, haikuText, breakable=True)
text = RichText((Mm(180), Mm(20)), None, haikuText)


##################################
##################################
# animation

startTime = time.time()

def setStartTime():
    startTime = time.time()
    return(startTime)

def countTime():
    timeNow = time.time()
    return(timeNow)


def refresh_func(time):
    #random.seed()
    #randPosX = random.random()
    #sinPos = math.sin((time / 2)) * 10
    #e2.y = Mm(sinPos)
    #print(startTime)
    thisTime = countTime()
    linePos = (thisTime-startTime)*6 # higher final number = more movement
    #print(linePos)
    l1.x = Mm(linePos)
    if linePos > 20.0:
        #print("hello")
        nowTime = setStartTime()
        print(nowTime)
        linePos = (thisTime-nowTime)*4
#print(linePos)









# function to make a single ting
def oneting(xPos, yPos, length, height):
    oneting = Path((Mm(xPos), Mm(yPos)), None, "#00000055", rotation=180)
    oneting.line_to(Mm(length), Mm(-abs(height)))
    oneting.line_to(Mm(length), Mm(height))
    oneting.close_subpath()



# single tings
#
# xPos, yPos, length, height
#oneting(120, 40, 10, 2)
#oneting(124, 30, 8, 3)


def manytings(num, posXLength, posYHeight, posX, posY, posXOffSet, posYOffSet):
    random.seed()
    for i in range(1, num):
        randPosX = random.random()
        randPosY = random.random()
        randXLength = random.random()
        randYHeight = random.random()
        oneting(posX*randPosX+posXOffSet, posY*randPosY+posYOffSet, posXLength*randXLength, posYHeight*randYHeight)

# num, length, height (-height <> height), xPos, yPos, xoffset, yoffset
manytings(20, 25, 2, 120, 40, 80, 80)



arcs_parent = PositionedObject((Mm(1), Mm(60)), None)


inc = (2 * math.pi) / 10
for i in range(1, 1):
    angle = i * inc
    #pos = Point(Mm(18 * (i - 1)), Mm(10))
    #pos = Point(Mm(18 * (i - 1)), Mm(10))
    #print(pos)
    randSizeFactorW = random.random()
    randSizeFactorH = random.random()
    randPosX = (random.random() * (i*4))
    print(randPosX)
    randPosY = (random.random() * (i*4))
        #arc = Path.arc(
        #pos, arcs_parent, Mm(12), Mm(8), angle, 0, Brush(Color(255, 255, 0, int(40*randColour)))
        #)
    
    Path.ellipse(
                   (Mm(randPosX), Mm(randPosY)), None, Mm((1*randSizeFactorW)+1), Mm((1*randSizeFactorH)+1), "#000000"
                   )
    # Draw origin +
    # Path.straight_line((ZERO, Mm(-0.5)), arc, (ZERO, Mm(1)))
    # Path.straight_line((Mm(-0.5), ZERO), arc, (Mm(1), ZERO))
    # Label angle
# Text((ZERO, Mm(-4)), arc, f"θ={angle:.2f}"

#################################
#################################

pageNum = 1


haikuText = haiku()
#text = Text((Mm(50), Mm(-10)), None, haikuText, breakable=True)
#text = RichText((Mm(50), Mm(-10)), None, haikuText)



RichText((Mm(0), Mm(0)), neoscore.document.pages[1], haikuText)


# ellipse as path
# as described in ellipse source
ellipse = Path((Mm(100), Mm(200)), neoscore.document.pages[1], "#00000055", rotation=45)
width=4
height=10
kappa = 0.5522848
ox = (width / 2) * kappa
oy = (height / 2) * kappa
xe = width
ye = height
xm = width / 2
ym = height / 2
ellipse.cubic_to(Mm(ZERO), Mm(ym - oy), Mm(xm - ox), Mm(ZERO), Mm(xm), Mm(ZERO))
ellipse.cubic_to(Mm(xm + ox), Mm(ZERO), Mm(xe), Mm(ym - oy), Mm(xe), Mm(ym))
ellipse.cubic_to(Mm(xe), Mm(ym + oy), Mm(xm + ox), Mm(ye), Mm(xm), Mm(ye))
ellipse.cubic_to(Mm(xm - ox), Mm(ye), Mm(ZERO), Mm(ym + oy), Mm(ZERO), Mm(ym))



# num, length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation
manyEllipses(40, pageNum, 3, 3, 120, 40, 40, 100, 360)
















#render_example("shapes")

if __name__ == "__main__":
    neoscore.show(refresh_func)




#Path.ellipse_from_center(
#    (Mm(20), Mm(10)),
#    None,
#   Mm(20),
#   Mm(10),
#   "#f004",
#   Pen(thickness=Mm(randColour)),
#)

#Path.arrow((Mm(40), Mm(20)), None, (Mm(40), Mm(10)))
#Path.straight_line((Mm(10), Mm(10)), None, (Mm(10), Mm(200)))




#Path.rect(
#    (Mm(0), Mm(35)),
#    None,
#    Mm(10),
#    Mm(16),
#    Brush(Color(0, 0, int(255*randColour), int(140*randColour))),
#    Pen(thickness=Mm(0.5)),
#)




#ting = Path(ORIGIN, None, "#0000ff55", rotation=180)
#ting.line_to(Mm(-1), Mm(1), text)
#ting.line_to(Mm(-1), Mm(12), text)
#ting.close_subpath()

#ting2 = Path(ORIGIN, None, "#0000ff55", rotation=180)
#ting2.line_to(Mm(-1), Mm(1), ting)
#ting2.line_to(Mm(-1), Mm(12), ting)
#ting2.close_subpath()


#ting3 = Path((Mm(40), Mm(0)), None, "#00000055", rotation=180)
#ting3.line_to(Mm(30), Mm(-4))
#ting3.line_to(Mm(30), Mm(4))
#ting3.close_subpath()

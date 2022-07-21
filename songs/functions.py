# functions

import random

from neoscore.core import neoscore
from neoscore.core.path import Path
from neoscore.core.units import ZERO, Mm
from neoscore.core.color import Color




##################################
# sticks


def oneStick(xPos, yPos, parent, length, height, color, rotation):
    #oneStick = Path((Mm(xPos), Mm(yPos)), None, "#964B00FF", rotation=0)
    oneStick = Path((Mm(xPos), Mm(yPos)), parent, color, rotation=rotation)
    oneStick.line_to(Mm(length), Mm(0))
    oneStick.line_to(Mm(length), Mm(height))
    oneStick.line_to(Mm(0), Mm(height))
    oneStick.line_to(Mm(0), Mm(0))

# oneStick(10, 10, neoscore.document.pages[pageNum], 15, 3, Color(165, 42, 42, 255), 76)




def manySticks(num, parent, xMin, xMax, yMin, yMax, length, height, rgba, alphaRand, rotation):
    random.seed()
    for i in range(0, num):
        randPosX = random.random()
        randPosY = random.random()
        randXLength = random.random()
        randYHeight = random.random()
        xPos = ((xMax-xMin)*randPosX)+xMin
        yPos = ((yMax-yMin)*randPosY)+yMin
        newAlpha = int(rgba[3] * random.random())
        color = Color(rgba[0], rgba[1], rgba[2], newAlpha)
        # newRotation = rotation * rotationRand
        newRotation = rotation[0] + ((rotation[1] - rotation[0]) * random.random())
        oneStick(xPos, yPos, neoscore.document.pages[parent], length*randXLength, height*randYHeight, color, newRotation)

# Example
# Color(165, 42, 42, 255)
# num, parent (pageNum), xMin, xMax, yMin, yMax, length, height, rgba, alphaRand, rotation, rotationRand
# manySticks(20, 0, 210, 240, 60, 90, 15, 3, [165, 42, 42, 255], 0.9, [358, 362])











##################################
# tings

# function to make a single ting
def oneting(xPos, yPos, parent, length, height):
    oneting = Path((Mm(xPos), Mm(yPos)), parent, "#00000055", rotation=180)
    oneting.line_to(Mm(length), Mm(-abs(height)))
    oneting.line_to(Mm(length), Mm(height))
    oneting.close_subpath()


# single tings
#
# xPos, yPos, length, height
#oneting(120, 40, 10, 2)
#oneting(124, 30, 8, 3)


def manytings(num, parent, posXLength, posYHeight, posX, posY, posXOffSet, posYOffSet):
    random.seed()
    for i in range(1, num):
        randPosX = random.random()
        randPosY = random.random()
        randXLength = random.random()
        randYHeight = random.random()
        oneting(posX*randPosX+posXOffSet, posY*randPosY+posYOffSet, neoscore.document.pages[parent], posXLength*randXLength, posYHeight*randYHeight)

# num, parent, length, height (-height <> height), xPos, yPos, xoffset, yoffset
# manytings(20, 0, 25, 2, 120, 40, 80, 80)





##################################
# ellipses

def oneEllipse(xPos, yPos, parent, width, height, rotation, color):
    ellipse = Path((Mm(xPos), Mm(yPos)), parent, color, rotation=rotation)
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
    return ellipse

# oneEllipse(120, 40, 10, 2, 45)

def manyEllipses(num, parent, posXLength, posYHeight, xPos, yPos, posXOffSet, posYOffSet, rotation, color):
    random.seed()
    #ellipseList = []
    for i in range(1, num):
        randPosX = random.random()
        randPosY = random.random()
        randXLength = random.random()
        randYHeight = random.random()
        randRotation = random.random()
        oneEllipse(xPos*randPosX+posXOffSet, yPos*randPosY+posYOffSet, neoscore.document.pages[parent], posXLength*randXLength, posYHeight*randYHeight, rotation*randRotation, color)


# num, parent, length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation
# manyEllipses(40, neoscore.document.pages[1], 3, 3, 120, 40, 40, 100, 360)


# create a horizontal line of ellipses
def lineHOfEllipses(num, parent, posXLength, posYHeight, xPos, yPos, posXOffSet, posYOffSet, rotation, color):
    random.seed()
    for i in range(1, num):
        randPosX = random.random()
        randPosY = random.random()
        randXLength = random.random()
        randYHeight = random.random()
        randRotation = random.random()
        oneEllipse(xPos*randPosX+posXOffSet+(i*4), posYOffSet, neoscore.document.pages[parent], posXLength*(randXLength*0.2)+2, posYHeight*(randYHeight*0.2)+2, rotation*randRotation, color)


# num, page (parent), length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation, color
# lineHOfEllipses(10, 1, 3, 3, 0, 0, 0, 10, 90, "#000000ff")


# create a vertical line of ellipses (chord)
def lineVOfEllipses(num, parent, posXLength, posYHeight, xPos, yPos, posXOffSet, posYOffSet, rotation, color):
    random.seed()
    for i in range(1, num):
        randPosX = random.random()
        randPosY = random.random()
        randXLength = random.random()
        randYHeight = random.random()
        randRotation = random.random()
        oneEllipse(posXOffSet, yPos*randPosY+posYOffSet+posXOffSet+(i*4), neoscore.document.pages[parent], posXLength*(randXLength*0.2)+2, posYHeight*(randYHeight*0.2)+2, rotation*randRotation, color)


# num, length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation
# lineVOfEllipses(10, pageNum, 3, 3, 0, 0, 10, 10, 45)


def stones(num, xPos, yPos):
    for i in range(1, num):
        randSizeFactorW = random.random()
        randSizeFactorH = random.random()
        #randPosX = ((random.random() * (i*2))+xPos)
        #randPosY = ((random.random() * (i*2))+yPos)
        randPosX = ((random.random() * (i*2.6))+xPos)
        randPosY = ((random.random() * (i*2.6))+yPos)
        
        stones = Path.ellipse(
                              (Mm(randPosX), Mm(randPosY)), None, Mm((2*randSizeFactorW)+1), Mm((2*randSizeFactorH)+1), "#000000"
                              )

#def oneStick(xPos, yPos, parent, width, height, rotation, color):
#   stick = Path((Mm(xPos), Mm(yPos)), parent, color, rotation=rotation):


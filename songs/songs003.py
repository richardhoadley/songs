# expressive materials
# percussion and melody instrument

#

import math
import random
import time
import pyOSC3

#from helpers import render_example

from neoscore.core import neoscore

from neoscore.core.directions import DirectionY
from neoscore.core.flowable import Flowable
from neoscore.core.font import Font
from neoscore.core.layout_controllers import MarginController
from neoscore.core.music_text import MusicText
from neoscore.core.text import Text
from neoscore.core.units import ZERO, Mm
from neoscore.western.barline import Barline
from neoscore.western.beam_group import BeamGroup
from neoscore.western.brace import Brace
from neoscore.western.chordrest import Chordrest
from neoscore.western.clef import Clef
from neoscore.western.duration import Duration
from neoscore.western.dynamic import Dynamic
from neoscore.western.instrument_name import InstrumentName
from neoscore.western.key_signature import KeySignature
from neoscore.western.staff import Staff
from neoscore.western.staff_group import StaffGroup
from neoscore.western.system_line import SystemLine
from neoscore.western.time_signature import TimeSignature

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

from typing import Tuple

#from functions import stones, oneEllipse, manyEllipses, lineHOfEllipses, lineVOfEllipses
from functions import *
from haiku import haiku


client = pyOSC3.OSCClient()
client.connect( ( '127.0.0.1', 57120 ) )
msg = pyOSC3.OSCMessage()
msg.setAddress("/print")
msg.append(500)
client.send(msg)



#neoscore.setup()
neoscore.setup(paper=Paper(Mm(297), Mm(210), Mm(10), Mm(10), Mm(10), Mm(10)))


# cd '/Users/rich/Documents/music/neoscore/neoscore-main/songs/' && '/usr/local/bin/python3'  '/Users/rich/Documents/music/neoscore/neoscore-main/songs/songs003.py'

pageNum = 0


# SCORE ###################################################


expressive_font = Font("Lora", Mm(4), italic=True)

flowable = Flowable((Mm(0), Mm(0)), None, Mm(500), Mm(30), Mm(10), Mm(20))
# Indent first line
flowable.provided_controllers.add(MarginController(ZERO, Mm(20)))
flowable.provided_controllers.add(MarginController(Mm(1), ZERO))

staff_group = StaffGroup()
# upper_staff = Staff((Mm(60), Mm(160)), flowable, Mm(120), staff_group)
upper_staff = Staff((Mm(60), Mm(160)), flowable, Mm(40), staff_group)

upper_staff2 = Staff((Mm(120), Mm(155)), flowable, Mm(80), staff_group)

# We can use the same unit in the upper and lower staves since they
# are the same size
unit = upper_staff.unit
upper_clef = Clef(unit(0), upper_staff, "treble")
upper_clef2 = Clef(unit(0), upper_staff2, "treble")
#KeySignature(ZERO, upper_staff, "g_major")
#TimeSignature(ZERO, upper_staff, (3, 4))

#InstrumentName((upper_staff.unit(-3), brace.center_y), upper_staff, "Melody instrument", "mel")
InstrumentName((upper_staff.unit(-3), upper_staff.unit(2)), upper_staff, "Melody instrument", "mel")

Dynamic((unit(-4), unit(6.5)), upper_staff, "ff")
Text((unit(-1), unit(6.5)), upper_staff, "molto espressivo", expressive_font)



# title ###################################################
title = Text((Mm(110), Mm(8)), None, "Songs of stone, wood and metal", scale=1.5)


# graphics ###################################################

# the cursor
random.seed()
randColour = random.random()
#randSizeFactor = random.random()



#Path((Mm(0), Mm(0)), neoscore.document.pages[0], Brush(Color(255, 255, 0, int(40*randColour))), Pen(color="#00ff00", thickness=Mm(2.5)))

# NB pen thickness seems limited to 1? 1.5?
stick = Path.straight_line(
                          (Mm(110), Mm(80)),
                          None,
                          (Mm(10), Mm(0)),
                          None,
                           #Brush(Color(255, 255, 0, 255)),
                           Brush(color="#964B00"),
                          Pen(color="#964B00", thickness=Mm(2))
                          )

# the cursor
l1 = Path.straight_line(
                        (Mm(0), Mm(0)),
                        None,
                        (Mm(0), Mm(190)),
                        None,
                        Brush(Color(255, 255, 0, int(40*randColour))),
                        Pen(color="#ff0000", thickness=Mm(0.5)),
                        )


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
        #print(nowTime)
        linePos = (thisTime-nowTime)*4
#print(linePos)


######################################################################################################
# songs



# num, page (parent), length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation, color
lineHOfEllipses(10, pageNum, 3, 3, 0, 0, 0, 10, 30, "#000000ff")



# BAR 1 ###################################################

nPos = 0
nOffset = 0

Dynamic((unit(-4), unit(6.5)), upper_staff, "pp")
Text((unit(-1), unit(6.5)), upper_staff, "molto espressivo", expressive_font)

Chordrest(unit(0), upper_staff, ["g'"], Duration(1, 1))



# Upper staff notes
nPos = 0
nOffset = 20

Dynamic((unit(0), unit(6.5)), upper_staff2, "mf")
Text((unit(0), unit(6.5)), upper_staff2, "molto espressivo", expressive_font)

Chordrest(unit(0), upper_staff2, ["g'"], Duration(1, 2))
Chordrest(unit(8), upper_staff2, ["f#'"], Duration(1, 1))
Chordrest(unit(16), upper_staff2, ["ab"], Duration(1, 8))
Chordrest(unit(18), upper_staff2, ["g'"], Duration(1, 1))
Chordrest(unit(26), upper_staff2, ["f#'"], Duration(1, 2))
Chordrest(unit(30), upper_staff2, ["ab"], Duration(1, 1))

Clef(Mm(60), upper_staff2, 'bass')

group = [
         Chordrest(unit(46), upper_staff2, ["a,,"], Duration(1, 16)),
         Chordrest(unit(48), upper_staff2, ["b,,"], Duration(1, 16)),
         Chordrest(unit(50), upper_staff2, ["bb,,"], Duration(1, 16)),
         Chordrest(unit(52), upper_staff2, ["c#,"], Duration(1, 16)),
         ]

BeamGroup(group)




# num, parent, length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation
manyEllipses(10, pageNum, 4, 4, 20, 20, 40, 40, 60, "#444444ff")


# oneEllipse(120, 40, neoscore.document.pages[0], 10, 2, 45, "#ff0000ff")


#stones function is in functions.py
# num, xPos, yPos
stones(10, 80, 10)

stones(10, 120, 40)


haikuText = haiku()
#text = Text((Mm(50), Mm(-10)), None, haikuText, breakable=True)
text = RichText((Mm(180), Mm(20)), None, haikuText)






# num, parent, length, height (-height <> height), xPos, yPos, xoffset, yoffset
manytings(20, 0, 25, 2, 120, 40, 80, 80)




##################################
# sticks


# Color(165, 42, 42, 255)
# num, parent (pageNum), xMin, xMax, yMin, yMax, length, height, rgba, alphaRand, rotation, rotationRand
manySticks(20, 0, 210, 240, 60, 90, 15, 3, [165, 42, 42, 255], 0.9, [358, 362])







###################################################################################################
###################################################################################################
# page 2
###################################################################################################

pageNum = 1


# num, page (parent), length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation, color
lineHOfEllipses(10, pageNum, 3, 3, 0, 0, 0, 10, 90, "#000000ff")

lineVOfEllipses(4, pageNum, 5, 5, 0, 3, 60, -60, 45, "#000000ff")



haikuText = haiku()
#text = Text((Mm(50), Mm(-10)), None, haikuText, breakable=True)
#text = RichText((Mm(50), Mm(-10)), None, haikuText)



RichText((Mm(100), Mm(40)), neoscore.document.pages[1], haikuText)


# ellipse as path
# as described in ellipse source
ellipse = Path((Mm(10), Mm(20)), neoscore.document.pages[1], "#00000055", rotation=45)
width=4
height=4
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



# num, length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation, color
manyEllipses(40, pageNum, 3, 3, 120, 40, 40, 100, 360, "#000000ff")
























#render_example("shapes")

if __name__ == "__main__":
    #x = int(360)
    #y = int(360)
#neoscore.show(refresh_func, min_window_size=Tuple[x, y])
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



# num, length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation
# manyEllipses(5, neoscore.document.pages[0], 5, 5, 30, 0, 0, 0, 360)


# xPos, yPos, parent, width, height, rotation
#oneEllipse(10, 10, neoscore.document.pages[0], 3, 3, 360)
#oneEllipse(15, 10, neoscore.document.pages[0], 3, 3, 360)
#oneEllipse(20, 10, neoscore.document.pages[0], 3, 3, 360)
#oneEllipse(25, 10, neoscore.document.pages[0], 3, 3, 360)
#oneEllipse(30, 10, neoscore.document.pages[0], 3, 3, 360)


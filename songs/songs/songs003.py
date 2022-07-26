# expressive materials
# percussion and melody instrument

import math
import random
import time
import pyOSC3
import sys

from helpers import render_example

from neoscore.core import neoscore

from neoscore.core.directions import DirectionY
from neoscore.core.directions import DirectionX
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
from neoscore.western.hairpin import Hairpin
from neoscore.western.instrument_name import InstrumentName
from neoscore.western.key_signature import KeySignature
from neoscore.western.slur import Slur
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

from typing import Tuple # this is to try and make the window larger

#from functions import stones, oneEllipse, manyEllipses, lineHOfEllipses, lineVOfEllipses
from functions import *
from haiku import haiku


# OSC
client = pyOSC3.OSCClient()
client.connect( ( '127.0.0.1', 57120 ) )
msg = pyOSC3.OSCMessage()
msg.setAddress("/print")
msg.append(500)
client.send(msg)

pageWidth = 360
pageHeight = 250
margins = 10

#neoscore.setup()
#neoscore.setup(paper=Paper(Mm(pageWidth-(margins*2)), Mm(pageHeight-(margins*2)), Mm(margins), Mm(margins), Mm(margins), Mm(margins)))
neoscore.setup(paper=Paper(Mm(pageWidth), Mm(pageHeight), Mm(margins), Mm(margins), Mm(margins), Mm(margins)))



# cd '/Users/rich/Documents/music/neoscore/neoscore-main/songs/' && '/usr/local/bin/python3'  '/Users/rich/Documents/music/neoscore/neoscore-main/songs/songs003.py'

pageNum = 0

# title ###################################################
materials_list = list(["stone", "wood", "metal"])
random.shuffle(materials_list)
print(materials_list)
# Output 222

title = Text((Mm(120), Mm(12)), None, "Songs of " + materials_list[0] + ", " + materials_list[1] + " and " + materials_list[2], scale=1.5)

# the dividing line
l1 = Path.straight_line(
                        (Mm(0), Mm((pageHeight-(margins*2))*0.08)),
                        None,
                        (Mm((pageWidth-(margins*2))), Mm(0)),
                        None,
                        #Brush(Color(255, 255, 0, int(40*randColour))),
                        Brush(Color(200, 200, 200, 255)),
                        Pen(color="#ccccccff", thickness=Mm(3.5)),
                        )


# SCORE ###################################################


Text((Mm(5), Mm(((pageHeight-(margins*2))*0.08)+10)), None, "percussion", scale=1.1)

"""
r1 = Path.rect(
               #(Mm(4), Mm((pageHeight-(margins*2))*0.08)),
                        (Mm(2), Mm(20)),
                        None,
                        Mm(32),
                        Mm(14),
                        #Brush(Color(255, 255, 0, int(40*randColour))),
                        Brush(Color(255, 255, 255, 0)),
                        Pen(color="#aaaaaaff", thickness=Mm(1.2)),
                        )
                        """

r1 = Path.rect((Mm(2), Mm(20)), None, Mm(32), Mm(14), Brush(Color(255, 255, 255, 0)), Pen(color="#aaaaaaff", thickness=Mm(1.2)))



expressive_font = Font("Lora", Mm(4), italic=True)

flowable = Flowable((Mm(0), Mm(0)), None, Mm(500), Mm(30), Mm(10), Mm(20))
# Indent first line
flowable.provided_controllers.add(MarginController(ZERO, Mm(20)))
flowable.provided_controllers.add(MarginController(Mm(1), ZERO))

#flow = Flowable((Mm(0), Mm(0)), None, Mm(11000), Mm(30), Mm(10))


staff_group = StaffGroup()
#staff = Staff((Mm(0), Mm(0)), flow, Mm(10000), staff_group, Mm(1)) # for hairpins, slurs, etc?

# upper_staff = Staff((Mm(60), Mm(160)), flowable, Mm(120), staff_group)
upper_staff = Staff((Mm(30), Mm(160)), flowable, Mm(40), staff_group)
upper_staff2 = Staff((Mm(100), Mm(165)), flowable, Mm(100), staff_group)
#upper_staff3 = Staff((Mm(200), Mm(105)), flowable, Mm(80), staff_group)

# We can use the same unit in the upper and lower staves since they
# are the same size
unit = upper_staff.unit
unit2 = upper_staff.unit
#upper_clef = Clef(unit(0), upper_staff, "treble") # single note
upper_clef2 = Clef(unit2(0), upper_staff2, "treble") #melody
#upper_clef3 = Clef(unit(0), upper_staff3, "tenor") #line
#KeySignature(ZERO, upper_staff, "g_major")
#TimeSignature(ZERO, upper_staff, (3, 4))

#InstrumentName((upper_staff.unit(-3), brace.center_y), upper_staff, "Melody instrument", "mel")
InstrumentName((upper_staff.unit(-3), upper_staff.unit(2)), upper_staff, "melody", "mel")

#Dynamic((unit(-4), unit(6.5)), upper_staff, "ff")
#Text((unit(-1), unit(6.5)), upper_staff, "molto espressivo", expressive_font)






# graphics ###################################################






#Path((Mm(0), Mm(0)), neoscore.document.pages[0], Brush(Color(255, 255, 0, int(40*randColour))), Pen(color="#00ff00", thickness=Mm(2.5)))

# NB pen thickness seems limited to 1? 1.5?


"""
stick = Path.straight_line(
                          (Mm(110), Mm(80)),
                          None,
                          (Mm(10), Mm(0)),
                          None,
                           #Brush(Color(255, 255, 0, 255)),
                           Brush(color="#964B00"),
                          Pen(color="#964B00", thickness=Mm(2))
                          )
"""

# the cursor
l1 = Path.straight_line(
                        (Mm(0), Mm(0)),
                        None,
                        (Mm(0), Mm(pageHeight-(margins*2))),
                        None,
                        #Brush(Color(255, 255, 0, int(40*randColour))),
                        Brush(Color(255, 255, 0, 30)),
                        Pen(color="#ff0000", thickness=Mm(0.5)),
                        )



# the dividing line
Path.straight_line(
                        (Mm(0), Mm((pageHeight-(margins*2))*0.5)),
                        None,
                        (Mm((pageWidth-(margins*2))), Mm(0)),
                        None,
                        #Brush(Color(255, 255, 0, int(40*randColour))),
                        Brush(Color(200, 200, 200, 255)),
                        Pen(color="#ccccccff", thickness=Mm(3.5)),
                        )

Text((Mm(5), Mm(((pageHeight-(margins*2))*0.5)+10)), None, "melody instrument", scale=1.1)

r2 = Path.rect((Mm(2), Mm(((pageHeight-(margins*2))*0.5)+2)), None, Mm(48), Mm(14), Brush(Color(255, 255, 255, 0)), Pen(color="#aaaaaaff", thickness=Mm(1.2)))




##################################
##################################
# animation functions

startTime = time.time()

def setStartTime():
    startTime = time.time()
    return(startTime)

def countTime():
    timeNow = time.time()
    return(timeNow)


def refresh_func(time):
    """
    #random.seed()
    #randPosX = random.random()
    #sinPos = math.sin((time / 2)) * 10
    #e2.y = Mm(sinPos)
    #print(startTime)
    """
    thisTime = countTime()
    linePos = (thisTime-startTime)*6 # higher final number = more movement
    l1.x = Mm(linePos)
    if linePos > 20.0:
        nowTime = setStartTime()
        linePos = (thisTime-nowTime)*4


######################################################################################################
# songs

percVOffset = 20

# if dynamic rendering is used, the annotations on the first page need moving to the right:
if "d" in str(sys.argv[1]):
    dynOffset = 8
else:
    dynOffset = 0




# num, page (parent), length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation, color
lineHOfEllipses(random.randrange(6, 9, 1), pageNum, 3, 3, 0, 0, 10, 25+percVOffset, 30, "#000000ff")

lineHOfEllipses(random.randrange(4, 7, 1), pageNum, 3, 3, 0, 0, 15, random.randrange(32, 36, 1)+percVOffset, 45, "#000000ff")

if "a" in str(sys.argv[1]):
    Text((unit(-24 + dynOffset), unit(-68)), upper_staff, "lineHOfEllipses: horizontal line of ellipses", expressive_font, scale=0.8)




###########################################################
# WCPN
###########################################################
# BAR 1 ###################################################

# single note
#upper_staff = Staff((Mm(40), Mm(160)), flowable, Mm(40), staff_group)
upper_clef = Clef(unit(0), upper_staff, "treble") # single note

Text((unit(-1), unit(10.5)), upper_staff, "molto espressivo", expressive_font)

Chordrest(unit(0), upper_staff, ["g'"], Duration(1, 1))

pp = Dynamic((unit(0), unit(6.5)), upper_staff, "pp")
ppr = Dynamic((unit(18), unit(6.5)), upper_staff, "pp")
p = Dynamic((unit(10), unit(6.5)), upper_staff, "p")
hairpin = Hairpin((Mm(6), Mm(0)), pp, (Mm(-2), Mm(0)), p, DirectionX.RIGHT)
hairpin = Hairpin((Mm(6), Mm(0)), p, (Mm(-2), Mm(0)), ppr, DirectionX.LEFT)

#regular_text = Text((Mm(20), unit(-1)), 0, text="piu mosso", font=font)


"""
# see kitchen_sink
font = Font("Lora", Mm(2), weight=100, italic=True)
regular_text = Text((Mm(20), staff.unit(-1)), 0, text="piu mosso", font=font)
p = Dynamic((Mm(20), staff.unit(6)), staff, "p")
sfz = Dynamic.sfz((Mm(25), staff.unit(6)), staff)
hairpin = Hairpin((Mm(0), Mm(3)), p, (Mm(0), Mm(3)), sfz, DirectionX.RIGHT)
slur = Slur((Mm(0), Mm(0)), regular_text, (Mm(0), Mm(0)), sfz)
"""





# Upper staff notes
nPos = 0
nOffset = 20

Dynamic((unit(0), unit(6.5)), upper_staff2, "mf")
Text((unit(-1), unit(10.5)), upper_staff2, "molto espressivo", expressive_font)

slurStart = Chordrest(unit(0), upper_staff2, ["g'"], Duration(1, 2))
slurEnd = Chordrest(unit(8), upper_staff2, ["f#'"], Duration(1, 1))
Slur((ZERO, unit(-4)), slurStart.stem.end_point, slurEnd.extra_attachment_point, slurEnd, direction=DirectionY.UP)

slurStart = Chordrest(unit(16), upper_staff2, ["ab"], Duration(1, 8))
slurEnd = Chordrest(unit(18), upper_staff2, ["g'"], Duration(1, 1))
Slur((ZERO, unit(0)), slurStart.stem.end_point, slurEnd.extra_attachment_point, slurEnd, direction=DirectionY.UP)


slurStart = Chordrest(unit(26), upper_staff2, ["f#'"], Duration(1, 2))
slurEnd = Chordrest(unit(30), upper_staff2, ["ab"], Duration(1, 2))
# slur attaches to the lower side of a semi-breve?
Slur((ZERO, unit(-4)), slurStart.stem.end_point, slurEnd.extra_attachment_point, slurEnd, direction=DirectionY.UP)


Clef(Mm(60), upper_staff2, 'bass')

# slurs don't seem to work within this grouping situation...
group = [
         Chordrest(unit(46), upper_staff2, ["a,,"], Duration(1, 16)),
         Chordrest(unit(48), upper_staff2, ["b,,"], Duration(1, 16)),
         Chordrest(unit(50), upper_staff2, ["bb,,"], Duration(1, 16)),
         Chordrest(unit(52), upper_staff2, ["c#,"], Duration(1, 16)),
         #Slur((ZERO, unit(0)), slurStart.stem.end_point, slurEnd.extra_attachment_point, slurEnd, direction=DirectionY.UP)
         ]

BeamGroup(group)



# this is the 'line' based notation for the melody instrument
# these are the stave definition and the clef"
upper_staff3 = Staff((Mm(220), Mm(185)), flowable, Mm(100), staff_group)
upper_clef3 = Clef(unit(0), upper_staff3, "tenor") #line

# the lines themselves
line = Path((Mm(240), Mm(182)), neoscore.document.pages[0], Brush(color="#ffffff00"), Pen(color="#000000ff", thickness=Mm(1.5)))
line.line_to(Mm(20), Mm(0)) # from the above point to 20 to the right, 0 up or down,
line.line_to(Mm(20), Mm(10)) # from that point, 0 vertically (20-20) and 10 horizontally
line.line_to(Mm(40), Mm(10))


line = Path((Mm(290), Mm(190)), neoscore.document.pages[0], Brush(color="#ffffff00"), Pen(color="#000000ff", thickness=Mm(0.5)))
line.line_to(Mm(15), Mm(0)) #
line.line_to(Mm(15), Mm(-6)) #
line.line_to(Mm(29), Mm(-8)) # glissando from -6 to -8

##################################
# curves
##################################

random.seed()
curveSizeX = (10 + (5*random.random()))
curveSizeY = (4 + (2*random.random()))

curveListX = [ ]
curveListY = [ ]
for i in range(0, 9):
    curveListX.append(((curveSizeX*2)*random.random())-(curveSizeX*0.2))
    curveListY.append(((curveSizeY*2)*random.random())-curveSizeY)

curve = Path((Mm(325), Mm(188)), neoscore.document.pages[0], Brush(color="#ffffff00"), Pen(color="#000000ff", thickness=Mm(0.5)))
curve.cubic_to(Mm(curveListX[0]), Mm(curveListY[0]), Mm(curveListX[1]), Mm(curveListY[1]), Mm(curveListX[2]), Mm(curveListY[2]))
curve.cubic_to(Mm(curveListX[3]), Mm(curveListY[3]), Mm(curveListX[4]), Mm(curveListY[4]), Mm(curveListX[5]), Mm(curveListY[5]))
curve.cubic_to(Mm(curveListX[6]), Mm(curveListY[6]), Mm(curveListX[7]), Mm(curveListY[7]), Mm(curveListX[8]), Mm(curveListY[8]))




# num, parent, length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation
manyEllipses(10, pageNum, 4, 4, 20, 20, 60, 10+percVOffset, 60, "#444444ff")

if "a" in str(sys.argv[1]):
    Text((unit(-4 + dynOffset), unit(-76)), upper_staff, "a cluster of ellipses (see function).", expressive_font, scale=0.8)


# oneEllipse(120, 40, neoscore.document.pages[0], 10, 2, 45, "#ff0000ff")


#stones function is in functions.py
# num, xPos, yPos
stones(10, 100, 30+percVOffset)

stones(10, 140, 20+percVOffset)

if "a" in str(sys.argv[1]):
    Text((unit(28 + dynOffset), unit(-76)), upper_staff, "clusters of stones (see function).", expressive_font, scale=0.8)
    Text((unit(28 + dynOffset), unit(-73)), upper_staff, "these are different from 'ellipses'", expressive_font, scale=0.8)
    Text((unit(28 + dynOffset), unit(-70)), upper_staff, "ellipses can be rotated, whereas stones cannot", expressive_font, scale=0.8)









if "a" in str(sys.argv[1]):
    Text((unit(-8 + dynOffset), unit(-34)), upper_staff3, "auto-generated haiku using vocabularies based on references", expressive_font, scale=0.8)
    Text((unit(-8 + dynOffset), unit(-31)), upper_staff3, "to types of stone, metals, or woods", expressive_font, scale=0.8)
    Text((unit(-8 + dynOffset), unit(-28)), upper_staff3, "haikus could be read, interpreted, played back or simply inform the mood:", expressive_font, scale=0.8)

haikuText = haiku()
#text = Text((Mm(50), Mm(-10)), None, haikuText, breakable=True)
text = RichText((Mm(270), Mm(140)), None, haikuText)




# num, parent, length, height (-height <> height), xPos, yPos, xoffset, yoffset
manytings(20, 0, 35, 1.5, 70, 20, 50, 50+percVOffset)

if "a" in str(sys.argv[1]):
    Text((unit(-4 + dynOffset), unit(-36)), upper_staff, "a cluster of 'tings' to be played on resonating metal objects", expressive_font, scale=0.8)




##################################
# sticks


# Color(165, 42, 42, 255)
# num, parent (pageNum), xMin, xMax, yMin, yMax, length, height, rgba, alphaRand, rotation, rotationRand
manySticks(40, 0, 180, 280, 40+percVOffset, 60+percVOffset, 12, 4, [165, 42, 42, 255], 0.9, [358, 362])







###################################################################################################
###################################################################################################
# page 2
###################################################################################################

pageNum = 1


# the dividing line
Path.straight_line(
                   (Mm(0), Mm((pageHeight-(margins*2))*0.5)),
                   neoscore.document.pages[pageNum],
                   (Mm((pageWidth-(margins*2))), Mm((pageHeight-(margins*2))*0.5)),
                   neoscore.document.pages[pageNum],
                   #Brush(Color(255, 255, 0, int(40*randColour))),
                   Brush(Color(200, 200, 200, 255)),
                   Pen(color="#ccccccff", thickness=Mm(3.5)),
                   )

Text((Mm(5), Mm(((pageHeight-(margins*2))*0.5)+10)), None, "melody instrument", scale=1.1)




# num, page (parent), length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation, color
#lineHOfEllipses(10, pageNum, 3, 3, 0, 0, 0, 10, 90, "#000000ff")

lineVOfEllipses(3, pageNum, random.randrange(2, 4, 1), random.randrange(2, 4, 1), 0, random.randrange(-1, 1, 1), 20, random.randrange(9, 11, 1), 45, "#000000ff")
lineVOfEllipses(3, pageNum, 5, 5, 0, 0, 38, 10, 45, "#000000ff")
lineVOfEllipses(3, pageNum, 5, 5, 0, 0, 56, 10, 45, "#000000ff")
lineVOfEllipses(3, pageNum, 6, 5, 0, 0, 73, 10, 45, "#000000ff")


# this is the 'line' based notation for the melody instrument
# these are the stave definition and the clef"
staffCurve = Staff((Mm(20), Mm(180)), neoscore.document.pages[1], Mm(80), staff_group)
staffClef = Clef(unit(0), staffCurve, "tenor") #line

Dynamic((unit(-4), unit(-85)), staffCurve, "p")

if "a" in str(sys.argv[1]):
    Text((unit(0), unit(-98)), staffCurve, "'chords' of stones (or wood or metal)", expressive_font)
    Text((unit(0), unit(-95)), staffCurve, "technically, these are lineVOfEllipses (vertical lines of ellipses)", expressive_font)
    Text((unit(0), unit(-79)), staffCurve, "should amplitude be determined by ellipse size?", expressive_font)

haikuText = haiku()
RichText((Mm(260), Mm(80)), neoscore.document.pages[1], haikuText)

if "a" in str(sys.argv[1]):
    Text((unit(70), unit(-92)), staffCurve, "an elaborate cluster of stones, metal and wood", expressive_font)
    Text((unit(70), unit(-89)), staffCurve, "this would require a particular suspended percussion set up", expressive_font)

# num, length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation, color
manyEllipses(40, pageNum, 2, 2, 120, 20, 140, 40, 360, "#000000ff")

# num, parent, length, height (-height <> height), xPos, yPos, xoffset, yoffset
manytings(30, pageNum, 12, 1, 80, 15, 180, 30) # now without percussion v offset as title is not on second page

# Color(165, 42, 42, 255)
# num, parent (pageNum), xMin, xMax, yMin, yMax, length, height, rgba, alphaRand, rotationRand
manySticks(20, pageNum, 190, 280, 40, 60, 8, 2, [100, 42, 42, 255], 0.5, [358, 362])


###################################################################################################
###################################################################################################
# curves
###################################################################################################



curve = Path((Mm(10), Mm(3)), staffCurve, Brush(color="#ffffff00"), Pen(color="#000000ff", thickness=Mm(0.8)))
curve.cubic_to(Mm(10), Mm(-2), Mm(12), Mm(3), Mm(8), Mm(3))
curve.cubic_to(Mm(9), Mm(3), Mm(15), Mm(4), Mm(12), Mm(2))
curve.cubic_to(Mm(17), Mm(1), Mm(15), Mm(-2), Mm(18), Mm(2))

#curve = Path((Mm(265), Mm(22)), neoscore.document.pages[1], Brush(color="#ffffff00"), Pen(color="#000000ff", thickness=Mm(0.8)))
curve = Path((Mm(30), Mm(5)), staffCurve, Brush(color="#ffffff00"), Pen(color="#000000ff", thickness=Mm(0.8)))
curve.cubic_to(Mm(random.randrange(6, 12, 1)), Mm(random.randrange(-3, 3, 1)), Mm(random.randrange(10, 14, 1)), Mm(random.randrange(1, 5, 1)), Mm(random.randrange(6, 10, 1)), Mm(random.randrange(1, 5, 1)))
curve.cubic_to(Mm(random.randrange(6, 10, 1)), Mm(random.randrange(2, 4, 1)), Mm(random.randrange(14, 16, 1)), Mm(random.randrange(3, 5, 1)), Mm(random.randrange(11, 13, 1)), Mm(random.randrange(1, 3, 1)))
curve.cubic_to(Mm(random.randrange(12, 18, 1)), Mm(random.randrange(0, 2, 1)), Mm(random.randrange(14, 16, 1)), Mm(random.randrange(-3, -1, 1)), Mm(random.randrange(17, 19, 1)), Mm(random.randrange(1, 3, 1)))


curve = Path((Mm(50), Mm(2)), staffCurve, Brush(color="#ffffff00"), Pen(color="#000000ff", thickness=Mm(0.8)))
curve.cubic_to(Mm(random.randrange(5, 13, 1)), Mm(random.randrange(-4, 4, 1)), Mm(random.randrange(9, 15, 1)), Mm(random.randrange(2, 4, 1)), Mm(random.randrange(5, 11, 1)), Mm(random.randrange(-3, 3, 1)))
curve.cubic_to(Mm(random.randrange(7, 18, 1)), Mm(3), Mm(random.randrange(7, 18, 1)), Mm(4), Mm(random.randrange(7, 18, 1)), Mm(2))
curve.cubic_to(Mm(random.randrange(7, 18, 1)), Mm(1), Mm(random.randrange(7, 18, 1)), Mm(-2), Mm(random.randrange(7, 18, 1)), Mm(2))


# wiggles
"""
random_wiggles = [
                  random.choice(["wiggleRandom1", "wiggleRandom2", "wiggleRandom3", "wiggleRandom4"])
                  for i in range(8)
                  ]

MusicText((Mm(120), unit(4)), staffCurve, random_wiggles)
"""



###################################################################################################
# a different method
###################################################################################################




random.seed()
curveSizeX = (10 + (5*random.random()))
curveSizeY = (4 + (2*random.random()))

curveListX = [ ]
curveListY = [ ]
for i in range(0, 9):
    curveListX.append(((curveSizeX*2)*random.random())-curveSizeX)
    curveListY.append(((curveSizeY*2)*random.random())-curveSizeY)

curve = Path((Mm(310), Mm(30+percVOffset)), neoscore.document.pages[0], Brush(color="#ffffff00"), Pen(color="#000000ff", thickness=Mm(0.5)))
curve.cubic_to(Mm(curveListX[0]), Mm(curveListY[0]), Mm(curveListX[1]), Mm(curveListY[1]), Mm(curveListX[2]), Mm(curveListY[2]))
curve.cubic_to(Mm(curveListX[3]), Mm(curveListY[3]), Mm(curveListX[4]), Mm(curveListY[4]), Mm(curveListX[5]), Mm(curveListY[5]))
curve.cubic_to(Mm(curveListX[6]), Mm(curveListY[6]), Mm(curveListX[7]), Mm(curveListY[7]), Mm(curveListX[8]), Mm(curveListY[8]))


random.seed()
curveSizeX = (10 + (5*random.random()))
curveSizeY = (4 + (2*random.random()))

curveListX = [ ]
curveListY = [ ]
for i in range(0, 9):
    curveListX.append(((curveSizeX*2)*random.random())-curveSizeX)
    curveListY.append(((curveSizeY*2)*random.random())-curveSizeY)

curve = Path((Mm(330), Mm(30+percVOffset)), neoscore.document.pages[0], Brush(color="#ffffff00"), Pen(color="#000000ff", thickness=Mm(0.5)))
curve.cubic_to(Mm(curveListX[0]), Mm(curveListY[0]), Mm(curveListX[1]), Mm(curveListY[1]), Mm(curveListX[2]), Mm(curveListY[2]))
curve.cubic_to(Mm(curveListX[3]), Mm(curveListY[3]), Mm(curveListX[4]), Mm(curveListY[4]), Mm(curveListX[5]), Mm(curveListY[5]))
curve.cubic_to(Mm(curveListX[6]), Mm(curveListY[6]), Mm(curveListX[7]), Mm(curveListY[7]), Mm(curveListX[8]), Mm(curveListY[8]))





#curve = Path((Mm(60), Mm(0)), neoscore.document.pages[0], "#ffffffff", Pen(color="#000000ff", thickness=Mm(0.5)))
#curve.cubic_to(Mm(curveSizeX1), Mm(curveSizeY1), Mm(curveSizeX2), Mm(curveSizeY2), Mm(curveSizeX3), Mm(curveSizeY3))
#curve.cubic_to(Mm(curveSizeX4), Mm(curveSizeY4), Mm(curveSizeX5), Mm(curveSizeY5), Mm(curveSizeX6), Mm(curveSizeY6))
#curve.cubic_to(Mm(curveSizeX7), Mm(curveSizeY7), Mm(curveSizeX8), Mm(curveSizeY8), Mm(curveSizeX9), Mm(curveSizeY9))











# ellipse as path
# as described in ellipse source
"""
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
"""


# num, length, height (-height <> height), xPos, yPos, xoffset, yoffset, rotation, color
manyEllipses(40, pageNum, 2, 2, 110, 30, 120, 140, 360, "#000000ff")
Text((unit(50), unit(-25)), staffCurve, "sul pont., spiccatto, staccattisimmo, ad libitum, colla parte, amplitude according to ellipse size", expressive_font)
Dynamic((unit(50), unit(-10)), staffCurve, "ppp")




###################################################################################################
###################################################################################################
# rendering
###################################################################################################

if "d" in str(sys.argv[1]):
    neoscore.show(refresh_func)
else:
    render_example("songs003")


#render_example("songs003")



#if __name__ == "__main__":
    ##x = int(360)
    ##y = int(360)
    ##neoscore.show(refresh_func, min_window_size=Tuple[x, y])
#    neoscore.show(refresh_func)



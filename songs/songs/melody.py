from helpers import render_example

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

neoscore.setup()

expressive_font = Font("Lora", Mm(4), italic=True)

flowable = Flowable((Mm(0), Mm(0)), None, Mm(500), Mm(30), Mm(10), Mm(20))
# Indent first line
flowable.provided_controllers.add(MarginController(ZERO, Mm(20)))
flowable.provided_controllers.add(MarginController(Mm(1), ZERO))

staff_group = StaffGroup()
upper_staff = Staff((Mm(0), Mm(0)), flowable, Mm(500), staff_group)

# We can use the same unit in the upper and lower staves since they
# are the same size
unit = upper_staff.unit

upper_clef = Clef(unit(0), upper_staff, "treble")

KeySignature(ZERO, upper_staff, "g_major")

TimeSignature(ZERO, upper_staff, (3, 4))

#InstrumentName((upper_staff.unit(-3), brace.center_y), upper_staff, "Piano", "pno")

Dynamic((unit(-4), unit(6.5)), upper_staff, "ff")
Text((unit(-1), unit(6.5)), upper_staff, "molto espressivo", expressive_font)

# BAR 1 ###################################################

# Upper staff notes
Chordrest(unit(0), upper_staff, ["g'"], Duration(1, 2))
Chordrest(unit(4), upper_staff, ["f#'"], Duration(1, 1))
#Chordrest(unit(8), upper_staff, ["f#'"], Duration(1, 8))
#Chordrest(unit(8), upper_staff, [" "], Duration(1, 2))
Chordrest(unit(8), upper_staff, ["ab"], Duration(1, 8))
Chordrest(unit(9), upper_staff, ["g'"], Duration(1, 1))
Chordrest(unit(13), upper_staff, ["f#'"], Duration(1, 2))
Chordrest(unit(15), upper_staff, ["ab"], Duration(1, 1))


render_example("expressive materials")

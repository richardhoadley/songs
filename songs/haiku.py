# haiku generation function
# code originally from https://www.101computing.net/haiku-generator-in-python/
import random
from random import randint

from neoscore.core.path import Path
from neoscore.core.units import ZERO, Mm

#wordList1 = ["Enchanting", "Amazing", "Colourful", "Delightful", "Delicate"] #adjective
#wordList2 = ["visions", "distance", "conscience", "process", "chaos"] #noun
#wordList3 = ["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"] #adjective
#wordList4 = ["true", "dark", "cold", "warm", "great"] #adjective
#wordList5 = ["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]
#wordList6 = ["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]
#wordList7 = ["inspiration", "imagination", "wisdom", "thoughts"]


def haiku():
    wordList1 = ["Wooden", "Stony", "Metallic", "Crystalline", "Igneous", "Metamorphic", "Sedimentary", "Silicate"]
    wordList2 = ["stone", "pebble", "rock", "marble", "feldspar", "mineral", "quartz", "gem", "opal", "ruby", "flint"]
    wordList3 = ["Rough-cut", "Smooth", "Precious", "Bright", "Translucent", "Invaluable", "Brilliant", "Precious", "Craggy", "Worthless"]
    wordList4 = ["light", "hard", "dark", "brittle", "crumbly", "chalky"]
    wordList5 = ["habit", "hardness", "lustre", "diaphaneity", "colour", "streak", "tenacity", "cleavage", "fracture", "parting", "magnetism", "fluorescence", "radioactivity", "taste", "smell"]
    #wordList5 = ["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]
    wordList6 = ["Immovable", "Unbreakable", "Irreplaceable", "Massive", "Irrevocable"]
    wordList7 = ["inspiration", "imagination", "wisdom", "thoughts"]

    wordIndex1=randint(0, len(wordList1)-1)
    wordIndex2=randint(0, len(wordList2)-1)
    wordIndex3=randint(0, len(wordList3)-1)
    wordIndex4=randint(0, len(wordList4)-1)
    wordIndex5=randint(0, len(wordList5)-1)
    wordIndex6=randint(0, len(wordList6)-1)
    wordIndex7=randint(0, len(wordList7)-1)

#haiku = "<p>" + wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",</p><p>"
#haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",</p><p>"
#haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + ".</p>"
    
    haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",<BR>"
    haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",<BR>"
    haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + "."

    print(haiku)
    return(haiku)




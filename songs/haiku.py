# haiku generation function
# code originally from https://www.101computing.net/haiku-generator-in-python/
import random
from random import randint

from neoscore.core.path import Path
from neoscore.core.units import ZERO, Mm

"""
#original word lists
wordList1 = ["Enchanting", "Amazing", "Colourful", "Delightful", "Delicate"] # 3 syllable adjective
wordList2 = ["visions", "distance", "conscience", "process", "chaos"] #noun
wordList3 = ["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"] # 4 syllable adjective
wordList4 = ["true", "dark", "cold", "warm", "great"] #adjective
wordList5 = ["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]
wordList6 = ["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]
wordList7 = ["inspiration", "imagination", "wisdom", "thoughts"]
"""

def haiku():
    random.seed()
    num = random.randrange(0, 3, 1)
    
    if num == 0: # stone
        wordList1 = ["Stony", "Crystalline", "Igneous", "Metamorphic", "Sediment", "Silicate"] # 3
        wordList2 = ["shiver", "rock", "marble", "feldspar", "mineral", "quartz", "gem", "opal", "ruby", "flint"] # 2

        wordList3 = ["Rough-cut", "Smooth", "Precious", "Bright", "Translucent", "Invaluable", "Brilliant", "Precious", "Craggy", "Worthless"]
        wordList4 = ["light", "hard", "dark", "brittle", "crumbly", "chalky"]
        wordList5 = ["habit", "hardness", "lustre", "diaphaneity", "colour", "fracture", "parting", "taste", "smell"]

        wordList6 = ["Immovable", "Unbreakable", "Irreplaceable", "Massive", "Irrevocable"]
        wordList7 = ["inspiration", "imagination", "wisdom", "thoughts"]
    
    elif num == 1: # metal
        # 5
        wordList1 = ["Ironic", "Steely", "Metallic", "Metalloid", "Silvery"] # 3
        wordList2 = ["mirror", "sheeting", "anvil", "ringing", "clasping", "leaden", "needle"] # 2
    
        # 7
        wordList3 = ["Reflecting this", "Displaying a", "Anticipating", "Welding a", "Smelting the", "Titanium"] # 4
        wordList4 = ["sharp", "true", "flat", "cold", "hard", "dense"] # 1
        wordList5 = ["surface", "ringing", "shining", "iron", "copper", "cobalt", "cutting", "slicing", "steely", "magnetism", "fluorescence", "radioactivity"] # 2
    
        # 5
        wordList6 = ["Beautiful", "Unchanging", "Corrosive", "Resonant", "Corroding", "Chromium", "Manganese", "Resonant"] # 3
        wordList7 = ["silence", "liquid", "solid"] # 2
    
    elif num == 2:
        # 5
        wordList1 = ["Wooden limb", "Climbing branch", "Timberland", "Topiary"] # 3
        wordList2 = ["splinter", "shiver", "needle", "shred", "fragment", "shaving", "paring"] # 2
        
        # 7
        wordList3 = ["Arboreal", "Displaying a", "Trees that show us", "tenacity"] # 4
        wordList4 = ["sharp", "true", "flat", "cold", "hard", "dense"] # 1
        wordList5 = ["surface", "ringing", "shining", "iron", "copper", "cobalt", "cutting", "slicing"] # 2
        
        # 5
        wordList6 = ["Beautiful", "Ligneous"] # 3
        wordList7 = ["silence", "solid", "forest", "seedling", "sapling", "seedling"] # 2

    wordIndex1=randint(0, len(wordList1)-1)
    wordIndex2=randint(0, len(wordList2)-1)
    wordIndex3=randint(0, len(wordList3)-1)
    wordIndex4=randint(0, len(wordList4)-1)
    wordIndex5=randint(0, len(wordList5)-1)
    wordIndex6=randint(0, len(wordList6)-1)
    wordIndex7=randint(0, len(wordList7)-1)

    haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",<BR>"
    haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",<BR>"
    haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + "."

#print(haiku)
    return(haiku)

"""
    # original parsing
    #haiku = "<p>" + wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",</p><p>"
    #haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",</p><p>"
    #haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + ".</p>"
    """




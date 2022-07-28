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
        wordList1 = ["Stony", "Crystalline", "Igneous", "Metamorphic", "Sediment", "Silicate", "Amethyst", "Magmatic", "Carbonate"] # 3
        wordList2 = ["sliver", "marble", "feldspar", "quartz", "gem", "opal", "ruby", "flint", "quicklime", "limestone", "gypsum"] # 2

        wordList3 = ["Rough-cut", "Precious", "Mineral", "Translucent", "Brilliant", "Precious", "Craggy", "Brittle", "Friable", "Porous"] # 2
        wordList4 = ["light", "hard", "dark", "flint", "rock", "smooth", "shard", "salt", "taste", "smell", "coal", "glass", "quartz"] # 1
        wordList5 = ["habit", "hardness", "lustre", "colour", "fracture", "parting", "fissure"] # 2

        wordList6 = ["Immovable", "Unbreakable", "Irreplaceable", "Irrevocable", "Diaphanous"] # 4
        wordList7 = ["inspiration", "imagination", "crystal", "walls"]
    
    elif num == 1: # metal
        # 5
        wordList1 = ["Ironic", "Steely", "Metallic", "Metalloid", "Silvery", "Golden"] # 3
        wordList2 = ["mirror", "sheeting", "anvil", "ringing", "clasping", "leaden", "needle"] # 2
    
        # 7
        wordList3 = ["Reflecting this", "Displaying a", "Anticipating", "Welding a", "Smelting the", "Titanium", "Radioactive"] # 4
        wordList4 = ["sharp", "true", "flat", "cold", "hard", "dense"] # 1
        wordList5 = ["surface", "ringing", "shining", "iron", "copper", "cobalt", "cutting", "slicing", "steely", "magnetism", "fluorescence"] # 2
    
        # 5
        wordList6 = ["Beautiful", "Unchanging", "Corrosive", "Resonant", "Corroding", "Chromium", "Manganese", "Resonant"] # 3
        wordList7 = ["silence", "liquid", "solid", "spiral", "shard"] # 2
    
    elif num == 2:
        # 5
        wordList1 = ["Wooden limb", "Climbing branch", "Timberland", "Topiary"] # 3
        wordList2 = ["splinter", "shiver", "needle", "shred", "fragment", "shaving", "paring", "apple", "aspen", "sawdust", "softwood", "hardwood"] # 2
        
        # 7
        wordList3 = ["Arboreal", "Displaying a", "Trees that show us", "tenacity", "Alder buckthorn"] # 4
        wordList4 = ["sharp", "true", "flat", "cold", "hard", "dense", "hedge", "tree", "branch", "twig", "oak", "birch", "ash", "beech", "box", "bark"] # 1
        wordList5 = ["surface", "ringing", "shining", "sawing", "slicing"] # 2
        
        # 5
        wordList6 = ["Beautiful", "Ligneous"] # 3
        wordList7 = ["silence", "solid", "forest", "seedling", "sapling"] # 2

    wordIndex1=randint(0, len(wordList1)-1)
    wordIndex2=randint(0, len(wordList2)-1)
    wordIndex3=randint(0, len(wordList3)-1)
    wordIndex4=randint(0, len(wordList4)-1)
    wordIndex5=randint(0, len(wordList5)-1)
    wordIndex6=randint(0, len(wordList6)-1)
    wordIndex7=randint(0, len(wordList7)-1)

    haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",<BR>"
    haiku = haiku + " &nbsp;  &nbsp;  &nbsp;  &nbsp; " + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",<BR>"
    haiku = haiku + " &nbsp;  &nbsp;  &nbsp;  &nbsp;   &nbsp;  &nbsp;  &nbsp;" + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + "."

#print(haiku)
    return(haiku)

"""
    # original parsing
    #haiku = "<p>" + wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",</p><p>"
    #haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",</p><p>"
    #haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + ".</p>"
    """




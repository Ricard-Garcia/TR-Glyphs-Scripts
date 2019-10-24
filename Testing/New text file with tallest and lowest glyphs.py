# MenuTitle: Text file with tallest and lowest glyphs.
# -*- coding: utf-8 -*-

# Ricard Garcia - 14.10.2019
# Parts based on code by mekkablue (https://github.com/mekkablue)
# ---------------------------------------------------------------


__doc__="""
Generates a new text file in font's path with a report of the tallest and lowest glyphs.
"""


# ---------------------
# Modules
# ---------------------
from GlyphsApp import *
from drawBot import *
from random import randint
import textwrap
import os


# ---------------------
# Variables
# ---------------------
f = Glyphs.font
exportingGlyphs = [g for g in f.glyphs if g.export]
layer = Glyphs.font.selectedLayers


# ---------------------
# Engine
# ---------------------


# --------------------------
# Generating the sorted list 


# **********
# General
masterID = f.masters[0].id
glyphsHeights = [[g.name, g.layers[masterID].bounds.origin.y, g.layers[masterID].bounds.origin.y + g.layers[masterID].bounds.size.height, g.unicode] for g in exportingGlyphs]


# **********
# Tallest

# Sorted list using origin y + height
tallestPrevious = sorted( glyphsHeights, key=lambda x: -x[2] )[0:len(exportingGlyphs)]


#print "---------------------------------------------"
#print "Tallest glyphs \n"
tallestNext = ""
for g in tallestPrevious:
	if g[2] <= f.masters[0].capHeight:
		pass
	else:	
		g2append = "Uni.: %s ------- N: %s ------- yVal:%d \n" % (str(g[3]), str(g[0]), g[2]) 	
		tallestNext += g2append	
		#print(g2append)


# **********
# Lowest

#print "\n\n---------------------------------------------"
#print "Lowest glyphs \n"
lowestNext = ""
lowestPrevious = sorted( glyphsHeights, key=lambda x: x[1] )[0:len(exportingGlyphs)]
for g in lowestPrevious:
	#print(g)
	if g[1] >= f.masters[0].descender:
		pass
	else:
		g2append = "Uni.: %s ------- N: %s ------- yVal:-%d \n" % (str(g[3]), str(g[0]), -g[1]) 	
		lowestNext += g2append
		#print(g2append)


# --------------------------
# Generating the text file 

# -----------------------------------------------------
# Accessing the directory of the file
# Setting a variable for its path
fDirectory = os.path.dirname(f.filepath) # Only the directory
fName = os.path.basename(f.filepath) # Only the name
fNameParts = os.path.splitext(fName) # Split parts
fPath = f.filepath

# -----------------------------------------------------
# Generating a text file with the report 
NewfName = fNameParts[0] + ' tallest and lowest glyphs.txt' # Change extension
NewfPath = os.path.join(fDirectory, NewfName) # Change extension

# Title
fontHeights = "# %s Tallest and lowest glyphs\nby %s\n" % (fNameParts[0], f.designer)

fontHeights += "\n%s Master\n" % (f.selectedFontMaster.name)

# Adding text
fontHeights += "\n\n--------------------------------------------- \nTallest glyphs"
fontHeights += "\n---------------------------------------------\n\n"
fontHeights += tallestNext

fontHeights += "\n\n--------------------------------------------- \nLowest glyphs"
fontHeights += "\n---------------------------------------------\n\n"
fontHeights += lowestNext

# Opening and writing the file
newFile = open(NewfPath, 'w')
newFile.write(fontHeights.encode('utf8'))
newFile.close()


# ---------------------
# Test
# ---------------------
print("Done!")

# MenuTitle: New tab with tallest and lowest glyphs.
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic) - 14.10.2019
# Parts based on code by mekkablue (https://github.com/mekkablue)
# ---------------------------------------------------------------


__doc__="""
Opens a new tab with a report of the tallest and lowest glyphs taking the blackest master as reference.
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
blackestMaster = len(f.masters)-1


# ---------------------
# Engine
# ---------------------


# --------------------------
# Generating the sorted list 


# **********
# General
masterID = f.masters[blackestMaster].id
glyphsHeights = [[g.name, g.layers[masterID].bounds.origin.y, g.layers[masterID].bounds.origin.y + g.layers[masterID].bounds.size.height, g.unicode] for g in exportingGlyphs]


# **********
# Tallest

# Sorted list using origin y + height
tallestPrevious = sorted( glyphsHeights, key=lambda x: -x[2] )[0:len(exportingGlyphs)]




#print("---------------------------------------------")
#print("Tallest glyphs \n")
tallestNext = ""
for g in tallestPrevious:
	if g[2] <= f.masters[0].capHeight:
		pass
	else:	
		g2append = "Uni.: %s ------- N: %s ------- yVal:%d \n" % (str(g[3]), str(g[0]), g[2]) 	
		tallestNext += g2append	
		print(str(g[0]), str(g[2]))


# **********
# Lowest

#print("\n\n---------------------------------------------")
#print("Lowest glyphs \n")
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
# New tab 

combinationTab = ""
combinationTab += "--------------------\nTallest glyphs\n--------------------\n"

for g in tallestPrevious:
	if g[2] <= f.masters[0].capHeight:
		pass
	else:
		combinationTab += "/%s" % (str(g[0]))
	
	
combinationTab += "\n\n--------------------\nLowest glyphs\n--------------------\n"

for g in lowestPrevious:
	if g[1] >= f.masters[0].descender:
		pass
	else:
		combinationTab += "/%s" % (str(g[0]))
		#print(g2append)


# Open new tab
Font.newTab(combinationTab)


# ---------------------
# Test
# ---------------------
print("Done!")

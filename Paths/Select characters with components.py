# MenuTitle: Select characters with components
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (with special help from Rainer, Tosche and Mark) - 10.02.2019
# ---------------------------------------------------------------------------


__doc__="""
Select all of the characters that have components in it.
"""


# ---------------------
# Variables
# ---------------------
thisFont = Glyphs.font # frontmost font
thisMaster = thisFont.selectedFontMaster # active master
affectedGlyphs = []


# ---------------------
# Engine
# ---------------------
for thisGlyph in thisFont.glyphs:
	# the layer with the master ID is the layer for that master:
	currentLayer = thisGlyph.layers[thisMaster.id] 
	if currentLayer.components:
		affectedGlyphs.append(thisGlyph)
		
if affectedGlyphs:
	thisFont.selection = affectedGlyphs
else:
	Message(title="No Components Found", message="Could not fond any components in the current master.", OKButton="Too bad")


# ---------------------
# Test
# ---------------------
print("Done!")
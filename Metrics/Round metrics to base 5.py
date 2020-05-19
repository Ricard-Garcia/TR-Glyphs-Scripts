# MenuTitle: Round metrics to base 5.
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic) - 19.05.2019
# ---------------------------------------------------------------------------


__doc__="""
Rounds metrics to base 5 in all selected glyphs of the current master.
"""


# ---------------------
# Variables
# ---------------------
f = Glyphs.font


# ---------------------
# Engine
# ---------------------
# Function rounding a target number to base 5
def round2Five(number2Round):
	roundedNumber = int(round(number2Round/5.0)*5.0)
	return(roundedNumber)

# Iterate through selected glyphs in font
for g in f.selection:
	# Only accessing the layer of the current master
	gLayer = g.layers[f.selectedFontMaster.id]	

	# Assigning the rounded values to the current layer	
	gLayer.LSB, gLayer.RSB = round2Five(gLayer.LSB), round2Five(gLayer.RSB)
	
	#print(gLayer.LSB, g.name)	

	
# ---------------------
# Test
# ---------------------
print("Done!")
# MenuTitle: Monospaced - New tab with characters with negative metrics in the current master.
# -*- coding: utf-8 -*-

# Ricard Garcia (@Typerepublic) - 27.01.2020
# ------------------------------------------


__doc__="""
Opens a new tab with those characters in the current master that have negative values. 
Ideal for testing monospaced designs.
"""


# ---------------------
# Modules
# ---------------------
from GlyphsApp import *


# ---------------------
# Variables
# ---------------------
f = Glyphs.font
m = f.selectedFontMaster


# ---------------------
# Engine
# ---------------------

# Empty string used for the new tab
tabText = ""

# Iterating through all glyphs
for g in f.glyphs:
	# If one or both sides are negative
	if g.layers[m.id].LSB < 0 or g.layers[m.id].RSB < 0:
		tabText += "/%s " % (g.name)
	else:
		pass
		#print("All set with character: %s" 5 (g.name))


# Opening a new tab
f.newTab(tabText)



# ---------------------
# Test
# ---------------------
print("Done!")





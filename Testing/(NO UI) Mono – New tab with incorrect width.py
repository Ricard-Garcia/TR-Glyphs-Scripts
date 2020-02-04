# MenuTitle: Monospaced - New tab with characters with incorrect width
# -*- coding: utf-8 -*-

# Ricard Garcia (@Typerepublic) - 27.01.2020
# ------------------------------------------


__doc__="""
In the current master, opens a new tab with those characters not fitting the width of the monoespaced design (now set to 600 ems).
"""

# ---------------------
# TODO
# ---------------------
# Add UI asking the user the width.

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
	# If the width of the current layer is not equal to 600
	if g.layers[m.id].width != 600:
		tabText += "/%s " % (g.name)
		print(g.name)
	else:
		pass
		#print("All set with character: %s" % (g.name))


# Opening a new tab
f.newTab(tabText)



# ---------------------
# Test
# ---------------------
print("Done!")
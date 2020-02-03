# MenuTitle: Monospaced - New tab with a testing string for monospaced fonts.
# -*- coding: utf-8 -*-

# Ricard Garcia (@Typerepublic) - 27.01.2020
# ------------------------------------------


__doc__="""
Opens a new tab with a testing string using "bar" between each character in the current font.
"""

# ---------------------
# TOOD
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


for g in f.glyphs:
	spaceC = "bar"
	
	#tabText += "/%s /%s /%s /%s \n" % (g.name, spaceC, g.name, spaceC)
	tabText += "/%s/%s " % (spaceC, g.name)

			
		
# Opening a new tab
f.newTab(tabText)



# ---------------------
# Test
# ---------------------
print("Done!")





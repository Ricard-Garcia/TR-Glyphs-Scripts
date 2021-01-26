# MenuTitle: Spacing tab from selection | Uppercase 
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic) - 16.11.2020
# ---------------------------------------------------------------------------


__doc__="""
From all glyphs selected, creates a new tab using H & O.
"""


# ---------------------
# Variables
# ---------------------
f = Glyphs.font
tabText = ""

# ---------------------
# Engine
# ---------------------


for g in f.selection:
	tabText += "/%s HH/%s HOHO/%s OO \n" % (g.name, g.name, g.name)
	
# Open new tab
f.newTab(tabText)

	
# ---------------------
# Test
# ---------------------
print("Done!")
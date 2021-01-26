# MenuTitle: Spacing tab from selection | Lowercase 
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic) - 25.01.2020
# ---------------------------------------------------------------------------


__doc__="""
From all glyphs selected, creates a new tab using n & o.
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
	tabText += "/%s nn/%s nono/%s oo \n" % (g.name, g.name, g.name)
	
# Open new tab
f.newTab(tabText)

	
# ---------------------
# Test
# ---------------------
print("Done!")
#MenuTitle: Set glyph's name to its Unicode
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic)- 28.07.2019
# -----------------------------------------


__doc__="""
From selected glyphs, sets their names to their Unicode.
"""


# ---------------------
# Modules
# ---------------------
from GlyphsApp import *

# ---------------------
# Variables
# ---------------------
f = Glyphs.font

# ---------------------
# Clear log in Macro Panel
Glyphs.clearLog()


# ---------------------
# Engine
# ---------------------
for g in f.selection:
	if g.unicode == None:
		pass
	else:
		uName = g.unicode
		g.name = str(uName)

# ---------------------
# Test
# ---------------------
print("Done!")












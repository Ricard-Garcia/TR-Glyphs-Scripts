#MenuTitle: Fun
# -*- coding: utf-8 -*-
__doc__="""
Fun colors in Glyphs file.
"""

from random import randint

# ---------------------
# General variables
font = Glyphs.font
glyphs = font.glyphs


# ---------------------
# Generate glyphs
for g in glyphs:
		g.color = randint(0,11)

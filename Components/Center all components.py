# MenuTitle: Centers all components in the middle of the layer.
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic) - 28.12.2020
# ------------------------------------------

__doc__="""
From all selected layers, centers all components in the middle of the layer.
"""


# Clearing Macro Panel
Glyphs.clearLog()


# ---------------------
# Variables
# ---------------------
f = Glyphs.font


# ---------------------
# Engine
# ---------------------
from Foundation import NSMidX

for l in f.selectedLayers:
	for c in l.components:
		compPosition = c.position
		compPosition.x += l.width/2.0 - NSMidX(c.bounds)
		c.position = compPosition

		

# ---------------------
# Test
# ---------------------
print("Done!")


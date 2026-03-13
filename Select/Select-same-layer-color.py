# MenuTitle: Select same layer color
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia - 13.03.2026
# ------------------------------------------


__doc__ = """
From the current master, selects other layers with the same layer color
as the selected layers.
"""


# ---------------------
# Variables
# ---------------------
f = Glyphs.font
selectedLayerColor = f.selectedLayers[0].color
newSelection = []


# ---------------------
# Engine
# ---------------------
for g in f.glyphs:
	if (g.layers[f.selectedLayers[0].layerId].color == selectedLayerColor):
		newSelection.append(g)

f.selection = newSelection
# ---------------------
# Test
# ---------------------
print("Done!")


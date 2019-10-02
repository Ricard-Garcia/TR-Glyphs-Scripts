# MenuTitle: Select same color
# Ricard Garcia - 02.10.2019
# -------------------
# -*- coding: utf-8 -*-
__doc__="""
From a given glyph, selects other glyphs with the same color."""

# ---------------------
# Variables
# ---------------------

# Font 
f = Glyphs.font

# Empty list to append all characters with the same color
nextSelection = []


# ---------------------
# Engine
# ---------------------

# Loop iterating trhough the font to identify glpyhs with the same color
for s in f.selection:
	for g in f.glyphs:
		if s.color == g.color:
			nextSelection.append(g)
			
		else:
			pass
			
# Assigning the font selection to the new list of characters
f.selection = nextSelection


# ---------------------
# Loop
# ---------------------
print("Done")

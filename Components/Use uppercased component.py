# MenuTitle: Use uppercased component
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia - 27.04.2020 
# --------------------------

# ---------------------
# Variables
# ---------------------
f = Glyphs.font

# ---------------------
# Engine
# ---------------------
def titleName(glyph):
	oldName = glyph.name
	newName = oldName.title()
	return(str(newName))
	
for g in f.selection:
	layer = g.layers[f.selectedFontMaster.id]
	#print(g.name)
	if layer.paths > 0:
		layer.paths = []
	else:
		pass
	
	if layer.components > 0:
		layer.components = []

	else:
		pass
	
	layer.components.append(GSComponent(titleName(g)))
	
	
	print(titleName(g))
	
	
# ---------------------
# Test
# ---------------------
print("Done!")
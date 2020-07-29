# MenuTitle: Random mover
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic) - 15.07.2020 
# ------------------------------------------


__doc__="""
Moves randomly all nodes (oncurve and offcurve) in selected paths by 1em.
"""

# ---------------------
# Modules
# ---------------------
import random


# Clear Macro Panel
Glyphs.clearLog()


# ---------------------
# Variables
# ---------------------
f = Glyphs.font
selectedLayers = f.selectedLayers
diff = 1 # Ems randomly moved


# ---------------------
# Engine
# ---------------------
# Random mover function
def randomMover(x, y, diff = 1):
	x += random.randint( -diff, diff )
	y += random.randint( -diff, diff )
	
	xPath = random.randint( -diff, diff )
	yPath = random.randint( -diff, diff )
	
	return(x, y, xPath, yPath)

# Move randomly only the selected paths in the current layer
for thisL in selectedLayers:
	for p in thisL.paths:
		print(p)
		if p.selected == True:
			print(p.bounds.origin.x)
			pathX, pathY = p.bounds.origin.x, p.bounds.origin.y
			pathX, pathY = randomMover(pathX, pathY, 3 )[0], randomMover(pathX, pathY, 3 )[1]
			
			shiftMatrix = [1, 
				0, 
				0, 
				1,   
				randomMover(pathX, pathY,3)[2],
				randomMover(pathX, pathY,3)[3]] 
			
			p.applyTransform( shiftMatrix )
			print(p.bounds.origin.x)

				
			for i, n in enumerate(p.nodes):
				if i % 2 == 0:
					n.x, n.y = randomMover(n.x, n.y)[0], randomMover(n.x, n.y)[1]
					print("Yes")
				else:
					n.x, n.y = randomMover(n.x, n.y)[0], randomMover(n.x, n.y)[1]
					print("Nope")
		else:
			pass  


# ---------------------
# Test
# ---------------------
print("Done!")

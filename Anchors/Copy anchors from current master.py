# MenuTitle: Copy anchors from selected glyphs to the other masters
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic with help from Rainer) - 19.09.2020 
# --------------------------


__doc__="""
From the current master, copies all anchors in selected glyphs to the other masters.
"""

# ---------------------
# Modules
# ---------------------
# Copy anchors from first master
from AppKit import NSPoint


# ---------------------
# Variables
# ---------------------
# Font object
font = Glyphs.font
# Selected layers
selectedLayers = font.selectedLayers
# Current master ID to be used in layers
currentMaster = f.selectedFontMaster.id


# ---------------------
# Engine
# ---------------------
# Function to copy anchors
def	copyAnchor(thisLayer, anchorName, anchorX, anchorY):
	newAnchor = GSAnchor.alloc().init()
	newAnchor.name = anchorName
	thisLayer.addAnchor_( newAnchor )
	newPosition = NSPoint( anchorX, anchorY)
	newAnchor.setPosition_( newPosition )	

# Dictionary to store selected Glyphs
selectedGlyphs = {}


for l in selectedLayers:
	glyphName = l.parent.name
	#Appending key and value
	selectedGlyphs[glyphName] = l
	
# Test
#print(selectedGlyphs)

for m in font.masters:
	masterID = m.id
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", m.name)


	for s in selectedGlyphs:
		print(s)
		thisLayer = font.glyphs[s].layers[masterID]
		# Iterating through anchors in the current master
		for anchor in font.glyphs[s].layers[currentMaster].anchors:
			anchorName = anchor.name
			anchorX = anchor.position.x
			anchorY = anchor.position.y

			copyAnchor(thisLayer, anchorName, anchorX, anchorY)
			

# Pop-up notification
Glyphs.showNotification("Copy anchors", "Copied anchors to all masters")


# ---------------------
# Test
# ---------------------
print("Appended anchors")
print("Done!")
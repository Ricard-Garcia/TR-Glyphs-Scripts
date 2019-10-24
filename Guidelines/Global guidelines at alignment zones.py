# MenuTitle: Guides through all alignment zones
# -*- coding: utf-8 -*-

# Ricard Garcia - 05.11.2018 
# --------------------------


__doc__="""
Sets a global guideline in each alignment zone.
"""


# ---------------------
# Variables
# ---------------------
# Set the variable of current master
thisMaster = Font.selectedFontMaster


# ---------------------
# Engine
# ---------------------
# For each alignment zone in the current master
for az in thisMaster.alignmentZones:

	# Get alignment zone position + its size
	AlignZone = az.position + az.size
	guidelineOrigin = (0, AlignZone)
	print(AlignZone)

	# Set the variable for the guideline
	myGuideline = GSGuideLine()
	# Add position
	myGuideline.position = guidelineOrigin

	# Lock guide
	myGuideline.setLocked_(True)

	# Add position
	thisMaster.addGuideLine_( myGuideline )

	print ("Guideline at: %d"%AlignZone)

# Pop-up notification
Glyphs.showNotification("Guidelines", "Global guidelines set at alignment zones.")


# ---------------------
# Test
# ---------------------
print("Done!")
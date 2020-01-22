# MenuTitle: New Tab with Left and Right Kern Keys
# -*- coding: utf-8 -*-

# Ricard Garcia (@Typerepublic) - 24.10.2019
# ------------------------------------------


__doc__="""
Opens a new tab with left and right kern key characters.
"""


# ---------------------
# Variables
# ---------------------
f = Glyphs.font


# ---------------------
# Engine
# ---------------------

# List of exporting glyphs
exportingGlyphs = [g for g in f.glyphs if g.export]

# Empty liss to append the keys as strings
LKGList = []
RKGList = []

LKGText = ""
RKGText = ""

for g in exportingGlyphs:
	glyphLKG = g.leftKerningGroup
	glyphRKG = g.rightKerningGroup
	
	
	# Left Kerning Classes
	if glyphLKG != None:
		if glyphLKG not in LKGList:
			LKGList.append(str(glyphLKG))
			LKGText += "/%s  " % (str(glyphLKG))
			
			
	# Right Kerning Classes
	if glyphRKG != None:
		if glyphRKG not in RKGList:
			RKGList.append(str(glyphRKG))
			RKGText += "/%s  " % (str(glyphRKG))



# Title
tabText = "------------------------------\n Kerning keys for %s \n------------------------------\n" % (f.familyName)

# LKG Title
tabText += "\n\n Left Kerning Keys \n *******************************\n"
tabText += LKGText

# RKG Title
tabText += "\n\n Right Kerning Keys \n *******************************\n"
tabText += RKGText


# Opening new tab
Font.newTab(tabText)
	
		
# ---------------------
# Test
# ---------------------
print("Done!")

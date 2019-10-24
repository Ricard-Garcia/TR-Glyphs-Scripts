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
leftKernClasses = []
rightKernClasses = []

# Left Kerning Classes
for g in exportingGlyphs:
	if str(g.leftKerningGroup) in leftKernClasses:
		pass
	else:
		leftKernClasses.append(str(g.leftKerningGroup))
		
#print leftKernClasses

leftKernSelection = []
for c in leftKernClasses:
	for g in f.glyphs:
		if c == g.name:
			leftKernSelection.append(g)


# Right Kerning Classes
for g in exportingGlyphs:
	if str(g.rightKerningGroup) in rightKernClasses:
		pass
	else:
		rightKernClasses.append(str(g.rightKerningGroup))

#print rightKernClasses

rightKernSelection = []

for c in rightKernClasses:
	for g in f.glyphs:
		if c == g.name:
			rightKernSelection.append(g)


# Generating the string for a new tab
newTabString = " "
newTabString += "Left Kerning Keys \n----------------------------------\n"

# Adding left key characters
for lk in leftKernSelection:
	newTabString += lk.string

newTabString += "\n\n\n"

newTabString += "Right Kerning Keys \n----------------------------------\n"

# Adding right key characters
for rk in rightKernSelection:
	newTabString += rk.string

#print(newTabString)	

# Opening new tab
Font.newTab(newTabString)
	
		
# ---------------------
# Test
# ---------------------
print("Done!")

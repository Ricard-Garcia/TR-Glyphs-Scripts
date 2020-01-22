# MenuTitle: New Tab with All Kern Keys
# -*- coding: utf-8 -*-

# Ricard Garcia (@Typerepublic) - 24.10.2019
# ------------------------------------------


__doc__="""
Opens a new tab with all kern key characters.
"""


# ---------------------
# TODO
# ---------------------
# Improve how the script gets each kern group.


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
		
# Left Kerning Classes
for g in exportingGlyphs:
	if str(g.rightKerningGroup) in rightKernClasses:
		pass
	else:
		rightKernClasses.append(str(g.rightKerningGroup))
		

# Lists combined
leftKernClasses.extend(rightKernClasses)

finalList = []
for s in leftKernClasses:
	if str(s) in finalList:
		pass
	else:
		finalList.append(str(s))

#print sorted(finalList)


# Generate selection
newSelection = []

for g in f.glyphs:
	for c in finalList:
		if c == g.name:
			newSelection.append(g)

print(newSelection)		


# Generating the string for a new tab
newTab = " "
for nS in newSelection:
	newTab += nS.string
	

# Opening new tab
Font.newTab(newTab)

		
# ---------------------
# Test
# ---------------------
print("Done!")

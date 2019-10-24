# MenuTitle: New tab with 10 highest and lowest glyphs in current master
# -*- coding: utf-8 -*-

# Ricard Garcia (@Typerepublic) - 03.10.2019 
# Parts based on code by mekkablue (https://github.com/mekkablue)
# ---------------------------------------------------------------


__doc__="""
Reports highest and lowest glyphs for each master in the Macro Window.
"""


# ---------------------
# Variables
# ---------------------

# *****************************************************************************	
# ("Report Highest and Lowest Glyphs" from mekkablue modified) ****************
f = Glyphs.font
exportingGlyphs = [g for g in thisFont.glyphs if g.export]

Glyphs.clearLog()
Glyphs.showMacroWindow()

#print "Highest and lowest glyphs for %s\n" % thisFont.familyName
masterID = f.selectedFontMaster.id
glyphsBottomsAndTops = [[g.name, g.layers[masterID].bounds.origin.y, g.layers[masterID].bounds.origin.y + g.layers[masterID].bounds.size.height] for g in exportingGlyphs]

lowestSorted = sorted( glyphsBottomsAndTops, key=lambda x: x[1] )[0:10]

# Empty list for lowest glyphs' names (g[0])
lowestResult =  []

# Lowest sorted
for g in lowestSorted:
	#print(g[0])
	lowestResult.append(g[0])

highestSorted = sorted( glyphsBottomsAndTops, key=lambda x: -x[2] )[0:10]
highestResult = []

# Empty list for highest glyphs' names (g[0])
for g in highestSorted:
	#print(g[0])
	highestResult.append(g[0])

# *****************************************************************************	
# *****************************************************************************	

# Empty list to append each lowest and highest glyph
All = []

# Appending lowest characters to All's list
for l in lowestResult:
	for g in f.glyphs:
		if str(l) in g.name:
			All.append(g)
			
# Appending highest characters to All's list
for h in highestResult:
	for g in f.glyphs:
		if str(h) in g.name:
			All.append(g)

# Setting the All as the font selection
f.selection = All

# String to be used in the new tab
newString = ""

for gl in f.selection:
	newString = newString + gl.string
	
#print(newString)

# Opens new tab with the characters and a space between them
f.newTab(" ".join(newString))


# ---------------------
# Test
# ---------------------
print("Done!")

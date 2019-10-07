#MenuTitle: .ss01 from selected characters
# Ricard Garcia - ??.02.2018
# -------------------

# -*- coding: utf-8 -*-
__doc__="""
Creates new glyphs with .ss01 suffix from selected characters. Then update features.
"""

# ---------------------
# Variables
# ---------------------
font = Glyphs.font
glyphs = font.glyphs


# ---------------------
# Select glyphs
select_g = []
print(select_g)

for g in font.selection:
	print(g.name)
	select_g.append(g.name)
	#g.color = 6     # light blue
	
print(select_g)


# ---------------------
# Engine
# ---------------------
# ---------------------
# Generate glyphs
for g in select_g:
	if g+'.ss01' in glyphs:
		print "Glyph %s.ss01 already in font." % (g)
	else:
		newGlyph = font.glyphs[g].copy()
		newGlyph.name = g+'.ss01'
		font.glyphs.append(newGlyph)
		newGlyph.color = 6

# ---------------------
# Colour
# for g in glyphs:
# 	#print(g.name)
# 	if ".ss01" in g.name:
# 		g.color = 6     # light blue
# 	else:
# 		pass


# ---------------------
# Update features
for feature in font.features:
        if feature.automatic:
                feature.update()
                         
# ---------------------
# Clear log in Macro Panel
# Glyphs.clearLog()


# ---------------------
# Test
# ---------------------
print("Done!")
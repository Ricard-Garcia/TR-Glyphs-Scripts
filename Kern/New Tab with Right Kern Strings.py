# MenuTitle: New Tab with Right Kern Strings
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic) - 29.07.2019
# ------------------------------------------

__doc__="""
From current's selection, opens a new tab with right kern strings.
"""


# ---------------------
# Notes
# ---------------------
# Make it usable for both left and right kern keys.


# Clearing Macro Panel
Glyphs.clearLog()


# ---------------------
# Variables
# ---------------------
f = Glyphs.font

# ---------------------
# Lists
# ---------------------
UCList = []
lcList = []


# ---------------------
# Engine
# ---------------------

# Getting glyphs' subcategories
for g in f.glyphs:
	if g.subCategory == "Uppercase":
		UCList.append(str(g.name))
	
	elif g.subCategory == "Lowercase":		
		lcList.append(str(g.name))
		
		
# Uppercase kern tab
UCTab = " "
listRKG = []
UCMasterKerns = []

# Appending kern keys
for u in UCList:
	RKG = f.glyphs[str(u)].rightKerningGroup

	if RKG not in listRKG:
		listRKG.append(RKG)
		#UCMasterKerns.append(u)
		
	else:
		pass
		
# Generating the string		
for u in f.selection:
	if rkg != None:
		for i in listRKG:
			UCTab += "/%s /%s NNONN " % (u.name, i)	
	
	elif rkg == None:
		pass
		
	else:
		pass
					

# Opening a new tab with the new string
f.newTab(UCTab)


# ---------------------
# Test
# ---------------------


#print(UCList)
#print("\n")
#print("UC Master Kern:", UCMasterKerns)	
#print("\n")
#print(UCTab)
#print("\n")
#print(listRKG)
#print("\n")
print("Done!")


# MenuTitle: New tab with uppercase, small cap and lowercase
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia - 02.10.2019
# --------------------------


__doc__="""
Opens a new tab with the combination of uppercase, small cap and lowercase of each character.
"""


# ---------------------
# Variables
# ---------------------
outputString = " "


# ---------------------
# List
# ---------------------
listUC = []

for g in Font.glyphs:
	if g.subCategory == "Uppercase":
		listUC.append(g.name)
	else:
		pass

# ---------------------
# Test
# ---------------------
print("List done!")

# ---------------------
# Engine
# ---------------------
for bc in listUC:
	lc_letter = bc.lower()
	
	
	result =  "/%s /%s.smcp /%s  " % (bc, lc_letter, lc_letter) 
	
	#Add new line + result to outputString
	outputString += "\n" + result 

print(outputString)

# Open new tab with outputString	
Font.newTab(outputString)


# ---------------------
# Test
# ---------------------
print("Done!")

	
	
	
	
	
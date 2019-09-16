# MenuTitle: New tab with OHhamburgefontsiv randomized
# Ricard Garcia - 07.11.2018
# -------------------
# -*- coding: utf-8 -*-
__doc__="""
Creates a new tab with 10 random combinations of OHhamburgefontsiv.
"""
# --------------------------------
from random import randint

# List with letters ---------------------------
letters = [
    'a',
    'm',
    'b',
    'u',
    'r',
    'g',
    'e',
    'f',
    'o',
    'n',
    't',
    's',
    'i',
    'v'
    ]

#print(len(letters))

# Loop creating "words" ---------------------------
numberWords = 15
#lstWords = []
outputString = ""

for w in range(numberWords):
	for l in range(len(letters)):
	    randomLetter = randint(0, len(letters)-1)
	    #print(randomLetter)

	    if l == 0:
	    	string = 'OH'+letters[randomLetter]
	    else:
	    	string = string + letters[randomLetter]

	    letters.remove(letters[randomLetter])

	letters = [
		'a',
		'm',
		'b',
		'u',
		'r',
		'g',
		'e',
		'f',
		'o',
		'n',
		't',
		's',
		'i',
		'v'
		]

	print(string)
	

	outputString += "%s\n" % string

Font.newTab(outputString)

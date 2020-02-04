# MenuTitle: Monospaced - New tab with a testing string for monospaced fonts (UI).
# -*- coding: utf-8 -*-

# Ricard Garcia (@Typerepublic) - 03.02.2020
# ------------------------------------------


__doc__="""
Opens a new tab with a testing string using the selected character between each glyph in the current font.
"""

# ---------------------
# TOOD
# ---------------------
# Add UI asking the user the width.

Glyphs.clearLog()

# ---------------------
# Modules
# ---------------------
from GlyphsApp import *
from vanilla import *

# ---------------------
# Variables
# ---------------------
f = Glyphs.font
m = f.selectedFontMaster


# ---------------------
# Engine
# ---------------------

# Generating the object
class monospaceString( object ):
	
	def __init__(self):
		self.w = FloatingWindow((250, 70), "Chain creator with all glyphs")
		self.w.label = TextBox((10,10,-120, 20), "Character to use:")
		self.w.character2Use = EditText((-130, 10, -10, 20), "", sizeStyle='small')
		self.w.createButton = Button((10, -30, -10, 20), "Generate text", callback=self.generatestringCallback)
		
		self.w.open()		
		
	def generatestringCallback ( self, sender ):
		char = self.w.character2Use.get()
		print(char)
		
		# Empty string used for the new tab
		tabText = ""
		
		for g in f.glyphs:
	
			#tabText += "/%s /%s /%s /%s \n" % (g.name, spaceC, g.name, spaceC)
			tabText += "%s/%s " % (str(char), g.name)

		# Test print
		#print(tabText)

				
		# Opening a new tab
		f.newTab(tabText)	

# Calling the object
monospaceString()


# ---------------------
# Test
# ---------------------
print("Done!")

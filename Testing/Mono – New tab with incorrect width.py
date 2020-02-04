# MenuTitle: Monospaced - New tab with characters with incorrect width (UI).
# -*- coding: utf-8 -*-

# Ricard Garcia (@Typerepublic) - 03.02.2020
# ------------------------------------------


__doc__="""
In the current master, opens a new tab with those characters not fitting the width of the monoespaced design (now set to 600 ems).
"""

# ---------------------
# TODO
# ---------------------
# Add UI asking the user the width.

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
# Variables
# ---------------------
f = Glyphs.font
m = f.selectedFontMaster


# ---------------------
# Engine
# ---------------------

# Generating the object
class testWidth( object ):
	
	def __init__(self):
		self.w = FloatingWindow((250, 70), "Check monospaced width")
		self.w.label = TextBox((10,10,-120, 20), "Width (ems):")
		self.w.character2Use = EditText((-130, 10, -10, 20), "", sizeStyle='small')
		self.w.createButton = Button((10, -30, -10, 20), "Check current master's widths", callback=self.widthCheckCallback)
		
		self.w.open()		
		
	def widthCheckCallback( self, sender ):
		tabText = ""
		# Iterating through all glyphs
		for g in f.glyphs:
			# If the width of the current layer is not equal to 600
			if g.layers[m.id].width != 600:
				tabText += "/%s " % (g.name)
				print(g.name)
			else:
				pass
				#print("All set with character: %s" % (g.name))


		# Test print
		#print(tabText)
				
		# Opening a new tab
		f.newTab(tabText)	

# Calling the object
testWidth()


# ---------------------
# Test
# ---------------------
print("Done!")
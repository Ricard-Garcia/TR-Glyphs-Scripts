#MenuTitle: Change Category and Subcategory
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic)- 28.07.2019
# -----------------------------------------


__doc__="""
(UI) Changes the Category and/or Subcategory to all selected glyphs.
"""


# ---------------------
# Modules
# ---------------------
from GlyphsApp import *
from vanilla import *


# ---------------------
# Clear log in Macro Panel
Glyphs.clearLog()


class changeCategorySubcategory(object):
	"""GUI opening a window to change both Categories and Subcategories of current font's selection."""

	f = Glyphs.font
	# If there are selected glyphs
	if len(f.selection) > 0:
		def __init__(self):
			
			# General variables
			self.f = Glyphs.font
			editTextWidth = -150
			
			# Leading
			x = 0
			y = 0
		
			# TITLE  #
			self.w = FloatingWindow((300, 130), "Change Category and Subcategory")
			
			# Leading incremenet
			x += 10
			y += 15
			
			# ------------------------------------------------------	
			# CATEGORY  #
			self.w.label = TextBox((x, y, -120, 20), "Category name:")
			self.w.categoryText = EditText((editTextWidth, y, -10, 20), placeholder="New Category", sizeStyle='small')
			
			# Leading incremenet
			y += 20
			
			# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>	
			# LINE  #
			self.w.line = HorizontalLine((x, y, -10, 20))
			# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>	
			
			# Leading incremenet
			y += 20
			
			# SUBCATEGORY  #
			self.w.label2 = TextBox((x, y, -120, 20), "Subcategory name:")
			self.w.subCategoryText = EditText((editTextWidth, y, -10, 20), placeholder="New Subcategory", sizeStyle='small')
			
			# Leading incremenet
			y += 40
			
			# Category button
			self.w.updateButton = Button((x, y, -10, 20), "Update data", callback=self.updateDataCallback)
			# ------------------------------------------------------	

			# Open the UI
			self.w.open()

	
		# UPDATE DATA CALLBACK
		def updateDataCallback(self, sender):
			# Getting the typed category
			newCat = self.w.categoryText.get()
			# Getting the typed subcategory
			newSubCat = self.w.subCategoryText.get()
			
			# If there's no typed Category
			if len(newCat) == 0:
				print("No Category typed.")
				
			# If there's a Category typed iterate through all selected glyphs
			else:
				for g in self.f.selection:
					#print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>", g.name)
					g.storeCategory = True
					g.category = newCat
				print("Changed categories")
				

			# If there's no typed Subcategory
			if len(newSubCat) == 0:
				print("No Subcategory Typed.")
				
			# If there's a Category typed iterate through all selected glyphs
			else:
				for g in self.f.selection:
					#print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>", g.name)
					g.storeSubCategory = True
					g.subCategory = newSubCat
				print("Changed subcategories")
				
				
		
	# If there's no glyph selected	
	else:
			Message("Change Category and Subcategory", "Please select at least one glyph.", OKButton=None)	


# Calling the object
changeCategorySubcategory()


# ---------------------
# Test
# ---------------------
print("Done!")












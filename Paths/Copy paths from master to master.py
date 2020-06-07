#MenuTitle: Copy paths from master to master
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic with special help from Rainer @mekkablue) - 19.05.2020 
# -----------------------------------------------------------------------------------


__doc__="""
Copy paths from one master to another.
"""

# ---------------------
# Modules
# ---------------------
from GlyphsApp import *
import vanilla, math
import traceback
from AppKit import NSAffineTransform, NSAffineTransformStruct

class Path2NewMaster( object ):
	"""User interface"""
	
	def __init__( self ):
		self.listOfMasters = []
		self.updateListOfMasters() 
		
		# Window 'self.w':
		windowWidth  = 400
		windowHeight = 220
		windowWidthResize  = 500 # user can resize width by this value
		windowHeightResize = 0   # user can resize height by this value
		self.w = vanilla.FloatingWindow(
			( windowWidth, windowHeight ), # default window size
			"Steal Metrics", # window title
			minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
			maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
			autosaveName = "com.mekkablue.MetricsCopy.mainwindow" # stores last window position and size
		)
		
		# UI elements:
		linePos, inset, lineHeight = 12, 15, 22
		
		self.w.descriptionText = vanilla.TextBox( (inset, linePos+2, -inset, 14), u"Open two fonts and select glyphs in the target font.", sizeStyle='small', selectable=True )
		linePos += lineHeight
		
		
		self.w.text_anchor = vanilla.TextBox( (inset, linePos+2, 130, 17), "Transfer metrics from:", sizeStyle='small')
		self.w.from_font = vanilla.PopUpButton( (inset+130, linePos, -inset, 17), self.listOfMasterNames(), sizeStyle='small', callback=self.buttonCheck)
		
		linePos += lineHeight
		self.w.text_value = vanilla.TextBox( (inset, linePos+2, 130, 17), "To selected glyphs in:", sizeStyle='small')
		self.w.to_font = vanilla.PopUpButton( (inset+130, linePos, -inset, 17), self.listOfMasterNames()[::-1], sizeStyle='small', callback=self.buttonCheck)
		
		linePos += lineHeight
		self.w.lsb   = vanilla.CheckBox( ( inset, linePos-1, 80, 20), "LSB", value=True, callback=self.buttonCheck, sizeStyle='small' )
		self.w.rsb   = vanilla.CheckBox( ( inset+80, linePos-1, 80, 20), "RSB", value=True, callback=self.buttonCheck, sizeStyle='small' )
		self.w.width = vanilla.CheckBox( ( inset+80*2, linePos-1, 80, 20), "Width", value=False, callback=self.buttonCheck, sizeStyle='small' )
		self.w.lsb.getNSButton().setToolTip_("If enabled, will transfer values for left sidebearings.")
		self.w.rsb.getNSButton().setToolTip_("If enabled, will transfer values for right sidebearings.")
		self.w.width.getNSButton().setToolTip_("If enabled, will transfer values for advance widths.")
		
		
		linePos += lineHeight
		self.w.preferMetricKeys  = vanilla.CheckBox( (inset, linePos, -inset, 20), "Prefer (glyph and layer) metrics keys whenever available", value=False, sizeStyle='small', callback=self.buttonCheck )
		self.w.preferMetricKeys.getNSButton().setToolTip_("If enabled, will transfer the metrics key rather than the metric value, if a metrics key is persent in the source font.")
		
		linePos += lineHeight
		self.w.onlyMetricsKeys = vanilla.CheckBox( (inset*2, linePos-1, -inset, 20), u"Only transfer metrics keys (ignore LSB, RSB, Width)", value=False, callback=self.buttonCheck, sizeStyle='small' )
		self.w.onlyMetricsKeys.enable(False)
		self.w.onlyMetricsKeys.getNSButton().setToolTip_("If enabled, will only transfer metrics keys and not change any metric values. The checkboxes for LSB, RSB and Width will be disabled.")
		
		linePos += lineHeight
		self.w.ignoreSuffixes    = vanilla.CheckBox( (inset, linePos, 190, 20), "Ignore dotsuffix in source glyph:", value=False, sizeStyle='small', callback=self.buttonCheck )
		self.w.suffixToBeIgnored = vanilla.EditText( (inset+190, linePos, -inset, 20), ".alt", sizeStyle = 'small')
		self.w.suffixToBeIgnored.getNSTextField().setToolTip_(u"Will copy metrics from source glyph ‘eacute’ to target glyph ‘eacute.xxx’. Useful for transfering metrics to dotsuffixed glyph variants.")
		
		self.w.copybutton = vanilla.Button((-80-inset, -20-inset, -inset, -inset), "Transfer", sizeStyle='small', callback=self.copyMetrics)
		self.w.setDefaultButton( self.w.copybutton )
		
		if not self.LoadPreferences( ):
			self.outputError( "Could not load preferences at startup. Will resort to defaults." )
		
		self.w.open()
		self.w.makeKey()
		
		self.buttonCheck( None )



	def updateListOfMasters( self ):
		try:
			masterList = []
		
			for thisFont in Glyphs.fonts:
				for thisMaster in thisFont.masters:
					masterList.append( thisMaster )
			
			masterList.reverse() # so index accessing works as expected, and the default is: current font = target
			self.listOfMasters = masterList
		except:
			print(traceback.format_exc())
	
	def listOfMasterNames( self ):
		try:
			myMasterNameList = [ 
				"%i: %s - %s" % ( 
					i+1,
					self.listOfMasters[i].font.familyName,
					self.listOfMasters[i].name 
				) for i in range(len( self.listOfMasters ))
			]
			return myMasterNameList
		except:
			print(traceback.format_exc())
	
	def outputError( self, errMsg ):
		print("Steal Sidebearings Warning:", errMsg)
















f = Glyphs.font

mastersDict = {}

for i, fm in enumerate(f.masters):
	mastersDict[str(fm.name)] = fm.id
	
	
#print(mastersDict)

for g in f.selection:
	gLayer = g.layers[mastersDict["Black"]]
	#layer2Paste = gLayer.copyDecomposedLayer()
	#newGLayer.append(layer2Paste)
	
	newpaths = []
	for path in gLayer.paths:
		newpaths.append(path.copy())
			
		
	# Sidebearings
	lsb1, rsb1 = gLayer.LSB, gLayer.RSB
	print(lsb1, rsb1)		

    	
	newGLayer = g.layers[mastersDict["Condensed Black"]]
	for i, path in enumerate(newGLayer.paths):
		del(newGLayer.paths[i-1])
		print("Test")
		
		
	newGLayer.paths.extend(newpaths)
	print("Added paths")
	newGLayer.LSB, newGLayer.RSB = lsb1, rsb1






	Path2NewMaster()

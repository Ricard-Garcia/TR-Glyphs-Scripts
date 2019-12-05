# MenuTitle: Single glyphs animation generator
# -*- coding: utf-8 -*-

# Ricard Garcia (@Typerepublic) - 04.12.2019 
# ------------------------------------------


__doc__="""
From a given string generates an animation of each single glyph per each frame.
"""


# ---------------------
# Modules
# ---------------------
from GlyphsApp import *
from drawBot import *
from vanilla import *
import math
from AppKit import NSColor
import textwrap
import os


# ---------------------
# Empty stack for Drawbot
newDrawing()


# ---------------------
# Clear log in Macro Panel
Glyphs.clearLog()



class singleGlyphsAnimation( object ):
	"""GUI generating an animation with all selected characters in the Font level"""

	def __init__( self ):
		
		# Window sizes
		windowW = 350
		windowH = 320
		
		# UI elements
		linePos = 20
		margin = 20
		lineHeight = 23
		columnLine = 140
		print(columnLine)
		


		# Building window
		self.w = vanilla.FloatingWindow(
			 ( windowW, windowH ),
			 "Animation generator"
			 )

		# ·····················································

		# Title
		self.w.descriptionText = vanilla.TextBox( (margin, linePos-5, -margin, lineHeight), "Select the characters you want in the animation", sizeStyle = "small")
		# Opening the window
		self.w.open()
		
		# ·····················································
		
		
		
		linePos += lineHeight*1.4
		#self.w.line0 = HorizontalLine((margin, int(linePos+4), -margin, 1))
		#linePos += lineHeight

		
		
		# ·····················································
		
		# Page format (in pixels)
		self.w.pageFormatTitle = vanilla.TextBox((margin, linePos, -margin, lineHeight), "Set frame format (px):", sizeStyle = "small")
		
		# ·····················································

		# ColorWell
		self.w.ColorWellTitle = vanilla.TextBox((columnLine + 40, linePos, 200, lineHeight), "Set colors:", sizeStyle = "small")

		# ·····················································


		linePos += lineHeight
		# Width
		self.w.widthTitle = vanilla.TextBox((margin*3, linePos+2, 100, lineHeight), "Width", sizeStyle = "small") 
		self.w.widthUser = vanilla.EditText((110, linePos, 50, 20), "1920", sizeStyle = "small")
		#print(int(str(self.w.widthUser.get())))
		
		
		# Foreground color
		self.w.fgColorTitle = vanilla.TextBox((columnLine + margin*3, linePos+2, 100, lineHeight), "Foreground", sizeStyle = "small") 
		self.w.fgColorWell = vanilla.ColorWell((columnLine + 20 + 120, linePos, 50, 20), color = NSColor.colorWithCalibratedRed_green_blue_alpha_(255/255, 255/255, 255/255, 1))
		print(self.w.fgColorWell.get())
		linePos += lineHeight
		
		# Height
		self.w.heightTitle = vanilla.TextBox((margin*3, linePos+2, 100, lineHeight), "Height", sizeStyle = "small") 
		self.w.heightUser = vanilla.EditText((110, linePos, 50, 20), "1200", sizeStyle = "small")
		
		# Background color
		self.w.bgColorTitle = vanilla.TextBox((columnLine + margin*3, linePos+2, 100, lineHeight), "Background", sizeStyle = "small") 
		self.w.bgColorWell = vanilla.ColorWell((columnLine + 20 + 120, linePos, 50, 20), color = NSColor.colorWithCalibratedRed_green_blue_alpha_(0/255, 0/255, 0/255, 1))
		print(self.w.bgColorWell.get())

		
		# ·····················································


		linePos += lineHeight +3
		self.w.line = HorizontalLine((margin, int(linePos+12), columnLine, 1))
		self.w.line2 = HorizontalLine((columnLine + 40, int(linePos+12), -margin, 1))
		linePos += lineHeight


		# ·····················································

		# Frame duration title
		self.w.frameDurationTitle = vanilla.TextBox((margin, linePos+2, 200, lineHeight), "Set frame duration:", sizeStyle = "small") 
		
		# Enable show nodes
		self.w.showNodes = vanilla.CheckBox((columnLine + 40, linePos-2, -margin, lineHeight), "Show nodes", value = False, sizeStyle = "small")
		#print(self.w.showNodes.get())
		
		self.w.showNodes.getNSButton().setToolTip_("If enabled, it will show the nodes and handles instead of a filled version of the characters.")
		
		
		
		# Frame duration edit
		linePos += lineHeight
		self.w.frameTextEdit = vanilla.TextBox((margin*3, linePos+2, 100, lineHeight), "Fps", sizeStyle = "small") 
		self.w.frameDurationUser = vanilla.EditText((110, linePos, 50, 20), "10", sizeStyle = "small")


		# ·····················································


		linePos += lineHeight
		self.w.line3 = HorizontalLine((margin, int(linePos+15), -margin, 1))
		linePos += lineHeight


		# ·····················································
		
		# Saving file format
		self.w.savingFormatTitle = vanilla.TextBox((margin, int(linePos+10), columnLine, lineHeight), "Select the file format:", sizeStyle = "small")
		
		self.w.popUpFormat = PopUpButton((columnLine+10, linePos+7, -margin, 20),
                              [".gif", ".mov", ".jpg", ".pdf"],
                              callback=self.getForegroundColor)

		
		# ·····················································
		
		
		linePos += lineHeight * 3
		
		
		# ·····················································
		# Generate button
		
		self.w.generateAnimation = vanilla.Button((margin, linePos, -margin, lineHeight), "Generate animation", sizeStyle = "small", callback = self.generateAnimation)
		
	# Error message
	def outputError( self, errMsg ):
		print "Character set warning:", errMsg
				
	# Test button	
	def testButton( self, sender ):
		
		print("Test")		
		

	# Main button used to generate the animation
	def generateAnimation( self, sender ):
		print("Animation!")
		
		# ---------------------
		# Variables
		# ---------------------
		# Font object
		f = Glyphs.font
		#print(f.selectedLayers)


		# Selection
		selection = f.selection
		#print(selection)

		# Frame duration 
		fDuration = 20

		# Scale
		scaleUser = 60
		s = scaleUser/100

		# Current master ID
		masterID = f.selectedFontMaster.id

		# Randomize master's index
		#masterIndexRandom = random.randint(0,len(f.masters))
		#print(masterIndexRandom)


		# Get the selected layer
		layer = Glyphs.font.selectedLayers[f.masterIndex]
		    
		# String
		userString = f.selection

		# Amount of frames
		#frames = len(f.selection)

		# Frame duration
		#fDuration = self.w.frameTextEdit.get()


		# Page format (pixels)
		w, h = int(str(self.w.widthUser.get())), int(str(self.w.heightUser.get()))

		# Set visible nodes
		nodesActive = True 

		# Background color (CMYK)
		bgColor = [0, .90, .86, 0] # TR Red

		# Lettershapes colours (CMYK)
		fgColor = [0, 0, 0, .2]


		# ---------------------
		# Functions
		# ---------------------

		# Centered glyph
		def centeredGlyph(layer, scaleFactor, pageWidth, pageHeight):
		    
		    with savedState():
		        scale(scaleFactor)
		        layerW = layer.bounds.size.width
		        layerH = layer.bounds.size.height
		        
		    
		        newOriginX = ( pageWidth - layerW ) / 2
		        newOriginY = ( pageHeight - layerH ) / 2
		    
		    #print(newOriginX, newOriginY)
		    
		    return(newOriginX, newOriginY)


		# Drawing the nodes of each character
		def drawNodes(layer, diameter, color):

			radius = diameter / 2

			for j, path in enumerate(layer.paths):
			    	#print(i, path)
				
			    	for i, node in enumerate(path.nodes):
			    	    xNode, yNode = node.position
			    	    if node.type == "offcurve":
			    	        cmykFill(*bgColor)
			    	        strokeWidth(1)
			    	        stroke(1)
			    	        oval(
			    	            xNode - radius,
			    	            yNode - radius,
			    	            diameter,
			    	            diameter
			    	            )
			    	        cmykFill(*fgColor)		    
			    	    elif node.type == "curve":
			    	        fill(1)
			    	        oval(
			    	            xNode - radius,
			    	            yNode - radius,
			    	            diameter,
			    	            diameter
			    	            )
			    	        cmykFill(*fgColor)		    
				        
			    	        # Previous 3rd point
			    	        p3X, p3Y = path.nodes[i-3].position
				        
			    	        # Previous 2nd point
			    	        p2X, p2Y = path.nodes[i-2].position
				        
			    	        # Previous point
			    	        p1X, p1Y = path.nodes[i-1].position
				        
			    	        stroke(1)
			    	        line(
			    	            (p3X, p3Y),
			    	            (p2X, p2Y)
			    	            )
				            
			    	        line(
			    	            (p1X, p1Y),
			    	            (xNode, yNode)
			    	            )
				        
			    	        stroke(None)
				        
			    	    else:
			    	        fill(1)
			    	        oval(
			    	            xNode - radius,
			    	            yNode - radius,
			    	            diameter,
			    	            diameter
			    	            )
			    	        cmykFill(*fgColor)		    



		for g in selection:
		    
			newPage(w, h)
			frameDuration(1/fDuration)

			# Background

			cmykFill(*bgColor)
			rect(0,0,w,h)
			

			layer = g.layers[f.masterIndex]
			print(layer.parent)
			# Generating a new page/frame

			#fill(1)
			print(layer.parent.name)

			
			#print( layer.bounds.origin.x, layer.bounds.origin.y)


			X, Y = centeredGlyph(layer, s, w, h)

			with savedState():
			    #oval(width()/2, height()/2, 20, 20)
				scale(s, center =(width()/2, height()/2))

				translate(X-layer.bounds.origin.x , Y- layer.bounds.origin.y + layer.bounds.size.height * .06)

				

				if nodesActive == True:
					drawNodes(layer, 10, (0))
					strokeWidth(1)
					cmykStroke(0,0,0,.2)
					cmykFill(None)

					drawPath(layer.completeBezierPath)
					#for c in layer.components:
					    #drawPath(c.completeBezierPath)


				elif nodesActive == False:
					cmykFill(0,0,0,.2)
					strokeWidth(1)
					cmykStroke(None)
					drawPath(layer.completeBezierPath)

				else:
					print("Nodes problem")    
					pass

				#print(layer.bounds)
				#fill(0,0,1,.2)
				#rect(
				#	layer.bounds.origin.x,
				#	layer.bounds.origin.y,
				#	layer.bounds.size.width,
				#	layer.bounds.size.height
				#	)
        # ---------------------
        # Telling Drawbot the drawing is done
        endDrawing()


		# Closing the window
		self.w.close()

		# ································· 
		# Saving process 
		# ·································

		# -----------------------------------
		# Accessing the directory of the file
		fDirectory = os.path.dirname(f.filepath) # Only the directory
		fName = os.path.basename(f.filepath) # Only the name
		fNameParts = os.path.splitext(fName) # Split parts
		fPath = f.filepath

		# --------------------------------------
		# Generating a text file with the report 
		# Assigning a format
		self.w.popUpFormat.get()
		listOfFormats = [".gif", ".mov", ".jpg", ".pdf"]


		NewfName = fNameParts[0] + ' - Glyphs animation%s' % (listOfFormats[self.w.popUpFormat.get()]) # Change extension
		NewfPath = os.path.join(fDirectory, NewfName) # Change extension

		# Saving the .pdf
		saveImage(NewfPath)


		# ································· 
		# Glyphs' notification
		# ·································
		Glyphs.showNotification('Animation generator', 'Generated animation from selection in the current font')


		# ---------------------
		# Test
		# ---------------------
		print("Done")  




# Calling the object
singleGlyphsAnimation()



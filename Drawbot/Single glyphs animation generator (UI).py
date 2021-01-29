# MenuTitle: Single glyphs animation generator
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic) - 09.12.2019 
# ------------------------------------------


__doc__="""
From a given string generates an animation of each single glyph per each frame.
"""


# ---------------------
# Modules
# ---------------------
from GlyphsApp import *
from drawBot import *
from AppKit import NSColor
from decimal import Decimal
import vanilla, math
import textwrap
import os



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
        #print(columnLine)
        


        # Building window
        self.w = vanilla.FloatingWindow(
             ( windowW, windowH ),
             "Animation generator"
             )

        # Opening the window
        self.w.open()
        
        # ·····················································

        # Title
        self.w.descriptionText = vanilla.TextBox( (margin, linePos-5, -margin, lineHeight), "Select the characters you want in the animation", sizeStyle = "small")

        
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
        
        
        # ·····················································

        
        # Width
        self.w.widthTitle = vanilla.TextBox((margin*3, linePos+2, 100, lineHeight), "Width", sizeStyle = "small") 
        self.w.widthUser = vanilla.EditText((110, linePos, 50, 20), "1200", sizeStyle = "small")
        #print(int(str(self.w.widthUser.get())))
        
        
        # Foreground color
        self.w.fgColorTitle = vanilla.TextBox((columnLine + margin*3, linePos+2, 100, lineHeight), "Foreground", sizeStyle = "small") 
        self.w.fgColorWell = vanilla.ColorWell((columnLine + 20 + 120, linePos, 50, 20), color = NSColor.colorWithCalibratedRed_green_blue_alpha_(250/255, 250/255, 250/255, 1)) # Light grey (RGB)
        
        
        linePos += lineHeight
        
        
        # Height
        self.w.heightTitle = vanilla.TextBox((margin*3, linePos+2, 100, lineHeight), "Height", sizeStyle = "small") 
        self.w.heightUser = vanilla.EditText((110, linePos, 50, 20), "1200", sizeStyle = "small")
        
        
        # Background color
        self.w.bgColorTitle = vanilla.TextBox((columnLine + margin*3, linePos+2, 100, lineHeight), "Background", sizeStyle = "small") 
        self.w.bgColorWell = vanilla.ColorWell((columnLine + 20 + 120, linePos, 50, 20), color = NSColor.colorWithCalibratedRed_green_blue_alpha_(0/255, 0/255, 0/255, 1)) # TR red (RGB) = 227/255, 39/255, 39/255, 1
        #print(color)

        
        # ·····················································


        linePos += lineHeight +3
        self.w.line = vanilla.HorizontalLine((margin, int(linePos+12), columnLine, 1))
        self.w.line2 = vanilla.HorizontalLine((columnLine + 40, int(linePos+12), -margin, 1))
        linePos += lineHeight


        # ·····················································

        # Frame Duration Title 
        self.w.frameDurationTitle = vanilla.TextBox((margin, linePos+2, 200, lineHeight), "Set frame duration:", sizeStyle = "small") 
        
        # Resize Glyph Title
        self.w.resizeGlyphTitle = vanilla.TextBox((columnLine + 40, linePos+2, 200, lineHeight), "Set glyph scale:", sizeStyle = "small") 
        
        linePos += lineHeight
        
        # Frame Duration value 
        self.w.frameTextEdit = vanilla.TextBox((margin*3, linePos+2, 100, lineHeight), "Fps", sizeStyle = "small") 
        self.w.frameDurationUser = vanilla.EditText((110, linePos, 50, 20), "7", sizeStyle = "small")

        # Resize Glyph Value
        self.w.resizeGlyphTextEdit = vanilla.TextBox((columnLine + margin*3, linePos+2, 100, lineHeight), "Value", sizeStyle = "small") 
        self.w.resizeGlyphUser = vanilla.EditText((columnLine + 20 + 120, linePos, 50, 20), "50%", sizeStyle = "small")

        # ·····················································


        linePos += lineHeight
        self.w.line3 = vanilla.HorizontalLine((margin, int(linePos+15), columnLine, 1))
        self.w.line4 = vanilla.HorizontalLine((columnLine + 40, int(linePos+15), -margin, 1))
        linePos += lineHeight


        # ·····················································
        
        
        # Enable show nodes
        self.w.showNodes = vanilla.CheckBox((margin, linePos+5, -margin, lineHeight), "Show nodes", value = False, sizeStyle = "small")
        self.w.showNodes.getNSButton().setToolTip_("If enabled, it will show the nodes and handles instead of a filled version of the characters.")
        
        # Saving file format
        self.w.savingFormatTitle = vanilla.TextBox((columnLine + 40, int(linePos+10), columnLine, lineHeight), "File format:", sizeStyle = "small")
        
        self.w.popUpFormat = vanilla.PopUpButton((columnLine+110, linePos+7, -margin, 20),
                              [".mp4", ".gif", ".jpg", ".pdf"])

        
        # ·····················································
        
        linePos += lineHeight*1.2
        self.w.line5 = vanilla.HorizontalLine((margin, int(linePos+15), -margin, 1))
        linePos += lineHeight*1.4
        
        
        # ·····················································
        # Generate button

        self.w.generateAnimation = vanilla.Button((margin, linePos, -margin, lineHeight), "Generate animation", sizeStyle = "small", callback = self.generateAnimation)
    

    def outputError( self, errMsg ):
        print("Character set warning:", errMsg)   


    # Test button   
    def testButton( self, sender ):
        
        print("Test")       
        

    # Main button used to generate the animation
    def generateAnimation( self, sender ):
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
        fDuration = int(self.w.frameDurationUser.get())
        
        # Scale
        #print("Raw resize:", self.w.resizeGlyphUser.get())
        
        scaleUserUnprocessed = self.w.resizeGlyphUser.get()
        scaleUser = scaleUserUnprocessed.replace("%", "")
        #print("This is the percentage: ", type(scaleUser))
        s = int(scaleUser)  * .01
        #print("Scale factor", s)
        
        # Current master ID
        masterID = f.selectedFontMaster.id
        
        # Randomize master's index
        #masterIndexRandom = random.randint(0,len(f.masters))
        #print(masterIndexRandom)
        
        
        # Get the selected layer
        #layer = Glyphs.font.selectedLayers[f.masterIndex]
            
        # String
        userString = f.selection
        
        # Amount of frames
        #frames = len(f.selection)
        
        # Frame duration
        #fDuration = self.w.frameTextEdit.get()
        
        
        # Page format (pixels)
        wi, he = int(self.w.widthUser.get()), int(self.w.heightUser.get())
        
        
        # Getting the components of the color well (foreground)
        fgCW = self.w.fgColorWell.get()
        print(fgCW)
        redFG, greenFG, blueFG = fgCW.redComponent(), fgCW.greenComponent(), fgCW.blueComponent()
        print("Foreground:", redFG, greenFG, blueFG)
        
        # Getting the components of the color well (background)
        bgCW = self.w.bgColorWell.get()
        print(bgCW)
        redBG, greenBG, blueBG = bgCW.redComponent(), bgCW.greenComponent(), bgCW.blueComponent()
        print("Background:", redBG, greenBG, blueBG)
        
        
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
        
                heightHGlyph =  f.glyphs['H'].layers[0].bounds.size.height*scaleFactor
                baselinePos = ( (pageHeight - heightHGlyph) / 2  ) - height()*.08
        
            if layer.bounds.origin.y == 0:
                newOriginY = baselinePos
                    
            elif layer.bounds.origin.y > 0:
                newOriginY = baselinePos + layer.bounds.origin.y
        
            elif layer.bounds.origin.y < 0:
                newOriginY = baselinePos + layer.bounds.origin.y
        
            else:
                print("Other circumstances")
                
                
            return(newOriginX, newOriginY)
            #print(layer.parent.name, "New Y:" , newOriginY, "Descender:", layer.bounds.origin.y)
        
        
        # Drawing the nodes of each character
        def drawNodes(layer, diameter, scale):
        
            radius = diameter / 2
        
            for j, path in enumerate(layer.paths):
                    #print(i, path)
                
                    for i, node in enumerate(path.nodes):
                        xNode, yNode = node.position
                        if node.type == "offcurve":
                            #colorSpace("sRGB")
                            fill(redBG, greenBG, blueBG)
                            strokeWidth(2*scale)
                            stroke(redFG, greenFG, blueFG)
                            oval(
                                xNode - radius,
                                yNode - radius,
                                diameter,
                                diameter
                                )
                                
                            stroke(None)
                                      
                        elif node.type == "curve":
                            #colorSpace("sRGB")
                            fill(redFG, greenFG, blueFG)
                            oval(
                                xNode - radius,
                                yNode - radius,
                                diameter,
                                diameter
                                )
                            fill(redFG, greenFG, blueFG)          
                            strokeWidth(2)
                            # Previous 3rd point
                            p3X, p3Y = path.nodes[i-3].position
                        
                            # Previous 2nd point
                            p2X, p2Y = path.nodes[i-2].position
                        
                            # Previous point
                            p1X, p1Y = path.nodes[i-1].position
                        
                            stroke(redFG, greenFG, blueFG)
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
                            #colorSpace("sRGB")
                            fill(redFG, greenFG, blueFG)
                            oval(
                                xNode - radius,
                                yNode - radius,
                                diameter,
                                diameter
                                )
                            #colorSpace("sRGB")
                            fill(redFG, greenFG, blueFG)          
        
        newDrawing()
        
        
        for g in selection:
        
            newPage(wi, he)
            frameDuration(1/fDuration)

            
            
          
            # Background
            #print("Background", redBG, greenBG, blueBG)
            #colorSpace("sRGB")
            fill(float(redBG), float(greenBG), float(blueBG))
            rect(0,0,wi,he)
            
            #stroke(0,1,0)
            
            #line(
            #  (0, height()*.3),
            #   (width(), height()*.3)
            #   )
            
            #stroke(None)      
        
            layer = g.layers[f.masterIndex]
            #print(layer.parent.name)
        
            
        
            X, Y = centeredGlyph(layer, s, wi, he)
        
        
        
            
            scale(s, center =(width()/2, height()/2))
            translate(X-layer.bounds.origin.x , Y-layer.bounds.origin.y)
            
    
            if self.w.showNodes.get() == 1:
                #colorSpace("sRGB")
                fill(redBG, greenBG, blueBG,1)
                strokeWidth(1)
                stroke(redFG, greenFG, blueFG,1)
    
                drawPath(layer.completeBezierPath)
                drawNodes(layer, 5*s, s)

                #print("nodes")
    
    
            elif self.w.showNodes.get() == 0:
                #colorSpace("sRGB")
                fill(redFG, greenFG, blueFG)
                strokeWidth(1)
                drawPath(layer.completeBezierPath)
                #print("not-nodes")
    
            else:
                print("Nodes problem")    
                pass
        
                
        # ---------------------
        # Telling Drawbot the drawing is done
        endDrawing()
        
        # Closing the window
        #self.w.close()
        
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
        listOfFormats = [".mp4", ".gif", ".jpg", ".pdf"]
        
        
        NewfName = fNameParts[0] + ' - Single Glyphs animation%s' % (listOfFormats[self.w.popUpFormat.get()]) # Change extension
        NewfPath = os.path.join(fDirectory, NewfName) # Change extension
        
        # Saving the .pdf
        saveImage(NewfPath)
        
        
        # ································· 
        # Glyphs' notification
        # ·································
        Glyphs.showNotification('Animation generator', 'Generated animation from selection in the current font')



# Calling the object
singleGlyphsAnimation()



# ---------------------
# Test
# ---------------------
print("Done")  


# MenuTitle: Character set builder with UI
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic with special help from Gustavo Ferreira and Frederik Berlaen) - 02.06.2019 
# ------------------------------------------


__doc__="""
From the current font, generates a character set with the given instructions in the UI.
"""

# ---------------------
# Notes
# ---------------------
# Uses intances' drawings instead of masters' ones.

# ---------------------
# Modules
# ---------------------
from GlyphsApp import *
from drawBot import *
import vanilla, math
import textwrap
import os


# ---------------------
# Empty stack for Drawbot
newDrawing()


# ---------------------
# Clear log in Macro Panel
Glyphs.clearLog()

class characterSetBuilder( object ):
    """GUI generating a character set out of the current font"""


    def __init__ ( self ):
        self.listOfMasters = []
        self.updateListOfMasters() 

        # Window settings
        windowWidth = 470
        windowHeight = 390        


        # Values used when the window is rezied by the user 
        #windowWidthResize  = 500 
        #windowHeightResize = 10   
        self.pageFormats = ["A0", "A0Landscape", "A1", "A1Landscape", "A2", "A2Landscape", "A3", "A3Landscape", "A4", "A4Landscape", "A4Small", "A4SmallLandscape", "A5", "A5Landscape", "B4", "B4Landscape", "B5", "B5Landscape", "Executive", "ExecutiveLandscape", "Folio","FolioLandscape", "Ledger", "LedgerLandscape", "Legal", "LegalLandscape", "Letter", "LetterLandscape", "LetterSmall", "LetterSmallLandscape", "Quarto", "QuartoLandscape", "Statement", "StatementLandscape", "Tabloid", "TabloidLandscape"]
        

        # Building window
        self.w = vanilla.FloatingWindow(
            ( windowWidth, windowHeight ), # default window size
            "Build Character Set", # window title
            #minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
            #maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
            )

        # UI elements
        linePos, margin, lineHeight = 20, 15, 25
        columnLine = margin + 145


        # Description text
        self.w.descriptionText = vanilla.TextBox( (margin, linePos, -margin, 14), u"Select some glyphs and choose the instances you want to see in the character set.", sizeStyle='small', selectable=True )
        linePos += lineHeight*1.5


        # Text + list of masters
        self.w.text_anchor = vanilla.TextBox( (margin, linePos+2, 200, 17), "Set the character set in:", sizeStyle='small')
        self.w.master2Use = vanilla.List( (margin+180, linePos, -margin,268), self.listOfMasterNames(), selectionCallback=self.getMaster, allowsMultipleSelection=True, )
        #print(self.w.master2Use.getSelection()
        self.w.master2Use.enable(onOff=True)
        linePos += lineHeight
        

        # All instances
        self.w.allMasters = vanilla.CheckBox( ( margin*2, linePos-1, 200, 20), "All instances", value=False, sizeStyle='small', callback=self.buttonCheck ) 
        linePos += lineHeight*1.8

        self.w.line = vanilla.HorizontalLine((margin, linePos-10, columnLine, 1))
        linePos += lineHeight*.05

        # Number of columns
        self.w.colNumberLabel = vanilla.TextBox( (margin, linePos+3, 200, 17), "Number of columns:", sizeStyle='small' )
        self.w.colNumberEdit = vanilla.EditText( (margin+115, linePos, margin+30, 20), "20", sizeStyle = 'small' )
        linePos += lineHeight

        self.w.line2 = vanilla.HorizontalLine((margin, linePos+7, columnLine, 1))
        linePos += lineHeight*0.8
        
        # Page format Pop-up 
        self.w.pageFormatText = vanilla.TextBox( (margin, linePos, 200, 17), "Page format:", sizeStyle='small')
        linePos += lineHeight
        self.w.pageFormat = vanilla.PopUpButton((margin, linePos-2, columnLine, 20), self.pageFormats, callback=self.popupFormat)
        
        # Default value to A4
        self.w.pageFormat.set(8)
        linePos += lineHeight


        self.w.line3 = vanilla.HorizontalLine((margin, linePos+7, columnLine, 1))
        linePos += lineHeight-1
        
        # Enable/Disable grid
        self.w.rectangle = vanilla.CheckBox( ( margin, linePos-5, 200, 20), "Grid", value=False, sizeStyle='small') 
        self.w.rectangle.getNSButton().setToolTip_("Enable or disable rectangle around each glyph.")

        linePos += lineHeight

        self.w.line4 = vanilla.HorizontalLine((margin, linePos+3, columnLine, 1))
        linePos += lineHeight

        # Enable/Disable text
        self.w.glyphText = vanilla.CheckBox( ( margin, linePos-5, 200, 20), "Name & Unicode", value=False, sizeStyle='small') 
        self.w.glyphText.getNSButton().setToolTip_("If activated, prints each glyph's Name and Unicode value.")

        #print("Text",self.w.glyphText.get())
        linePos += lineHeight

        # Generate button
        self.w.buildChar = vanilla.Button( ( margin+180, windowHeight*.83, -margin, margin+lineHeight*2 ), "Generate", sizeStyle='small', callback=self.buildCharacterSet)


        # Opening the window
        self.w.open()
        self.w.makeKey()
        

    def getMaster( self, sender  ):
            print("testButton1")
    

    def buttonCheck( self, sender ):
        try:
            # enable Only Keys option only if 
            allMastersCheckBoxChecked = self.w.allMasters.get()
            print(allMastersCheckBoxChecked)

            if allMastersCheckBoxChecked == 1:
                self.w.master2Use.enable( onOff=False )
                print("Disabled list")
            elif allMastersCheckBoxChecked == 0:
                self.w.master2Use.enable( onOff=True )
                print("Enabled list")
            else:
                pass
            
        except:
            import traceback

            print(traceback.format_exc())

        
    # Update List of Masters
    def updateListOfMasters( self ):
        try:
            masterList = []
        
            for thisFont in Glyphs.fonts:
                for thisMaster in thisFont.instances:
                    masterList.append( thisMaster )
            
            #masterList.reverse() # so index accessing works as expected, and the default is: current font = target
            self.listOfMasters = masterList
        except:
            print(traceback.format_exc())


    # Names of masters
    def listOfMasterNames( self ):
        try:
            myMasterNameList = [ 
                "%s | %s" % ( 
                    self.listOfMasters[i].font.familyName,
                    self.listOfMasters[i].name 
                ) for i in range(len( self.listOfMasters ))
            ]
            return myMasterNameList
        except:
            print(traceback.format_exc())
    

    def outputError( self, errMsg ):
        print("Character set warning:", errMsg)


    # Page format
    def popupFormat(self, sender):
        #sortedPageFormats = pageFormats.sort()
        return(sender.get())
        
        
    # Build character set
    def buildCharacterSet(self, sender):
        # ---------------------
        # Variables
        # ---------------------

        # Font object
        f = Glyphs.font

        # List of exporting glyphs
        exportingGlyphs = [g for g in f.glyphs if g.export]

        # Selected layer
        layer = Glyphs.font.selectedLayers

        # Current master ID
        masterID = f.selectedFontMaster.id


        # ---------------------
        # Engine
        # ---------------------

        # Function drawing top and bottom lines
        def drawLinesTopBottom(w, h, margin):
            fill(None)
            strokeWidth(1)
            stroke(0)
            lineCap("round")
            lineDash(.25, 2.5)
            
            # Top line
            line((margin, h*0.95), (w-margin,h*0.95))
            
            # Bottom line
            line((margin, h*0.05), (w-margin,h*0.05))
            
            # Reset values
            stroke(None)
            lineDash(None)
            
            
        # Function setting each glyph's name and Unicode
        def glyphNameAndUnicode (glyphName, originX, boxWidth, originY, boxHeight, UnicodeValue):
            text(glyphName, (originX+boxWidth*.08, originY-boxHeight*.03))
            text(UnicodeValue, (originX+boxWidth*.08, originY-boxHeight*.11))


        # Function that draws each glyph
        def glyph2draw(layer, boxOrigin, boxWidth, boxHeight = 20, font = f):
            
            # Positions
            originX, originY = boxOrigin

            # Scale factor 
            scaleFactor = boxHeight/(f.masters[0].capHeight*2)
            #print("Scale factor = %s" % (scaleFactor))
            myCapHeight = f.glyphs['H'].layers[0].bounds.size.height
            #print(myCapHeight)
            
            # Colors
            fill(0)
            stroke(0)
            #strokeWidth(0)
            
            # ································· 
            # Text in each box
            # ································· 
            glyphName = FormattedString()
            glyphName.append(layer.parent.name, font="Barna-SemiBold", fontSize = boxHeight*.06, fill = (0))
            
            UnicodeValue = FormattedString()
            uniString = ""
            uniString = "%s" %(layer.parent.unicode)
            UnicodeValue.append(uniString, font="Barna-Light", fontSize = boxHeight*.06, fill = (0))
            
            # Any character that is a mark  
            if str(layer.parent.category) == "Mark":
                with savedState():
            
                   
                    # Dashed circle   
                    fill(None)
                    strokeWidth(25*scaleFactor)
                    stroke(0)
                    lineCap("round")
                    lineDash(.30*scaleFactor, 2)
                
                    oval(originX+boxWidth*.335, originY+boxHeight*.25, boxWidth//3, boxHeight//3) 
                   
                    
                    # Activate grid
                    if self.w.rectangle.get() == 1:
                        #print("Grid enabled")
                        
                        # Rectangle's colours
                        fill(None) 
                        strokeWidth(15*scaleFactor)   
                        # Black rectangle around     
                        rect(originX, originY-boxHeight*0.2, boxWidth, boxHeight*1.2)
                        
                    else:
                        #print("Grid disabled")
                        pass

                    # Text and glyph's color 
                    fill(0.3)
                    strokeWidth(15*scaleFactor)
                    stroke(1)


                    # Glyph text and Unicode        
                    if self.w.glyphText.get() == 1:     
                        # Writing each text (current glyph's name and its Unicode value) 
                        glyphNameAndUnicode (glyphName, originX, boxWidth, originY, boxHeight, UnicodeValue)
                        #print("Text activated")
  
                    elif self.w.glyphText.get() == 0:
                        #print("Text deactivated")
                        pass
                   

                # Drawing the glpyh
                with savedState():
                    scale(scaleFactor, scaleFactor, center = (originX, originY))
                    translate(originX, originY+(myCapHeight/2)) # * = unpacking tuple

                    translate(
                        ((boxWidth - layer.width * scaleFactor) / 2)/scaleFactor
                        )

                    drawPath(layer.completeBezierPath)
                    
                    
            # Other characters (and separator)
            if layer.bounds.size.width > 0 or str(layer.parent.category) == "Separator":
                with savedState():                     
                
                    # Activate grid
                    if self.w.rectangle.get() == 1:
                        #print("Grid enabled")
                        
                        # Rectangle's colours
                        fill(None) 
                        strokeWidth(15*scaleFactor)   
                        # Black rectangle around     
                        rect(originX, originY-boxHeight*0.2, boxWidth, boxHeight*1.2)
                        
                    else:
                        #print("Grid disabled")
                        pass

                    # Text and glyph's color 
                    fill(0.3)
                    strokeWidth(15*scaleFactor)
                    stroke(1)


                # Glyph's text and Unicode        
                    if self.w.glyphText.get() == 1:     
                        # Writing each text (current glyph's name and its Unicode value) 
                        glyphNameAndUnicode (glyphName, originX, boxWidth, originY, boxHeight, UnicodeValue)
                        #print("Text activated")
  
                    elif self.w.glyphText.get() == 0:
                        #print("Text deactivated")
                        pass
                    
                # Drawing the glpyh
                with savedState():
                    scale(scaleFactor, scaleFactor, center = (originX, originY))
                    translate(originX, originY+(myCapHeight/2)) # * = unpacking tuple

                    translate(
                        ((boxWidth - layer.width * scaleFactor) / 2)/scaleFactor
                        )

                    drawPath(layer.completeBezierPath)

            

            # If there's an empty cell        
            else:

                if self.w.rectangle.get() == 1:                        
                    #print("Grid activated")

                    # Rectangle's colours
                    fill(None)
                    strokeWidth(15*scaleFactor)
                
                    # Black rectangle around     
                    rect(originX, originY-boxHeight*0.2, boxWidth, boxHeight*1.2)

                else:
                    #print("Grid deactivated")
                    pass
                 
                strokeWidth(15*scaleFactor)
                # Dashed cross       
                lineCap("round")
                lineDash(.25, 2.5)  
                line(
                    (originX, originY - boxHeight * .2),
                    (originX + boxWidth, originY + boxHeight)
                    )
                    
                line(
                    (originX, originY + boxHeight),
                    (originX + boxWidth, originY - boxHeight * .2)
                    )

                lineDash(None)
                
                
                # Glyph's text and Unicode        
                if self.w.glyphText.get() == 1:     
                    # Writing each text (current glyph's name and its Unicode value) 
                    glyphNameAndUnicode (glyphName, originX, boxWidth, originY, boxHeight, UnicodeValue)
                    #print("Text activated")
  
                elif self.w.glyphText.get() == 0:
                    #print("Text deactivated")
                    pass
                    
                else:
                    pass



        # ---------------------
        # PDF 
        # ---------------------

        # ·····················
        # COVER
        # ·····················

        # New A4
        pageFormatIndex = self.w.pageFormat.get()
        selectedPageFormat = str(self.pageFormats[pageFormatIndex])
        print("Selected format: ", selectedPageFormat)
        newPage("%s" % (selectedPageFormat))

        # Unpacking its values
        w, h = width(), height()
        
        # Background
        #cmykFill(0, 90, 86, 0)
        #fill(1)
        #rect(0,0,w, h)

        # Margin set to the 10% of the width if it's not a Landscape format
        if "Landscape" in selectedPageFormat:
            margin = w*.05
            marginY = h*.05
            print("Landscape format")
        else:
            margin = w*.1
            marginY = h*.05
            
        

        # Prints
        #print("This is the width - margin", w-margin)
        #print("A4 sizes", sizes('A4'))


        # ---------------------
        # Text in the cover

        # Title
        coverInfo = FormattedString()
        coverInfo.append("%s\nCharacter set"%(str(f.familyName)), font="Barna-ExtraBold", fontSize = 24, fill = (0))
        text(coverInfo, (margin, h*0.90))

        # Designer and manufacturer
        coverInfo2 = FormattedString()
        coverInfo2.append("%s (%s)"%(f.designer, f.manufacturer), font="Barna-Light", fontSize = 12, fill = (0))
        text(coverInfo2, (margin, h*0.08))

        # Dashed lines
        drawLinesTopBottom(w, h, margin)


        # ································· 
        # CHARACTER SET
        # ·································

        # New page
        newPage(selectedPageFormat)

        # Background
        #cmykFill(0, 90, 86, 0)
        #fill(1)
        #rect(0,0,w, h)

        # Columns
        columns = int(self.w.colNumberEdit.get())
        boxWidth = (w-margin*2) / columns
        #print("Box width:", boxWidth)


        # -----------
        # Text on top

        # Typeface's name + "Character set"
        generalInfo = FormattedString()
        generalInfo.append("%s — Character set"%(str(f.familyName)), font="Barna-Regular", fontSize = 10, fill = (0))
        text(generalInfo, (margin, h*0.96))

        # Dashed lines
        drawLinesTopBottom(w, h, margin)

        # Point/Leading size
        size = boxWidth*.9
        leading = size*1.2

        # Column width
        columnWidth = w - margin*2

        # Extra space
        reduc = boxWidth * 1.2


        # Accessing the master
        mastersIndex = self.w.master2Use.getSelection()
        #print(mastersIndex)
        
        listOfMasters2 = []
        
        if self.w.allMasters.get() == 1:
           listOfMasters2 = f.instances
           
        else:    
            for m in mastersIndex:
                listOfMasters2.append(self.listOfMasters[ m ])
                #print(sourceMaster)
    
        #listOfMasters2.append(sourceMaster)



        # ----------------------
        # Drawing the characters

        # Origin positions
        originX = margin 
        originY = h - marginY*1.5  - size       

        # Loop count
        loop = 0

        selectedLayers = f.selectedLayers


        for thisLayer in selectedLayers:
            for m in listOfMasters2:

                instanceFont = m.interpolatedFontProxy

                instanceGlyph = instanceFont.glyphForName_(thisLayer.parent.name)
                pathToDraw = instanceGlyph.layers[instanceFont.fontMasterID()]
                #drawPath(instanceLayer.bezierPath)
            

                #pathToDraw = g.layers[m.id]
                
                if loop == 0:

                    # Drawing the glyph with its text
                    glyph2draw(pathToDraw, (originX, originY), boxWidth, size) 
                 
                else:
                    
                    # New page
                    # If its a landscape format
                    if "Landscape" in selectedPageFormat:
                        bottomMargin =  marginY*2.5
                    else:
                        bottomMargin =  marginY*2

                    if originX > w-margin - reduc and originY - size < bottomMargin:
                         #print("New page needed")                 
                         loop = 0
                         
                         originX = margin
                         originY = h - marginY*1.5 - size 

                         # New page
                         newPage(selectedPageFormat)                

                         # Dashed lines
                         drawLinesTopBottom(w, h, margin)

                         text(generalInfo, (margin, h*0.96))
                         
                        # Drawing the glyph with its text
                         glyph2draw(pathToDraw, (originX, originY), boxWidth, size)
                        
                        
                    # New line

                    elif originX >= w - margin - reduc:
                        #print('originX out of the page')
                                                    
                        originX = margin
                        originY = originY-leading
                        translate(0, 0)
                            
                        # Drawing the glyph with its text
                        glyph2draw(pathToDraw, (originX, originY), boxWidth, size) 
                        

                    else: 
                        originX = originX + boxWidth

                        # Function
                        glyph2draw(pathToDraw, (originX, originY), boxWidth, size)
         
                loop += 1


        # ---------------------
        # Telling Drawbot the drawing is done
        endDrawing()
        

        # ---------------------
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
        NewfName = fNameParts[0] + '-Character set-%s.pdf' % (selectedPageFormat) # Change extension
        NewfPath = os.path.join(fDirectory, NewfName) # Change extension

        # Saving the .pdf
        saveImage(NewfPath)


        # ································· 
        # Glyphs' notification
        # ·································
        Glyphs.showNotification('Character set builder', 'Generated character set of the current font')


        # ---------------------
        # Test
        # ---------------------
        print("Done")
        

# Calling the object
characterSetBuilder()

# MenuTitle: Character set builder
# -*- coding: utf-8 -*-

# Ricard Garcia (@Typerepublic) - 05.11.2019 
# ------------------------------------------


__doc__="""
From the current font
"""


# ---------------------
# Modules
# ---------------------

from GlyphsApp import *
from drawBot import *
from vanilla import *
from random import randint
import textwrap
import os

# ---------------------
# Empty stack for drawbot
newDrawing()

# ---------------------
# Clear log in Macro Panel
Glyphs.clearLog()


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
    strokeWidth(1)
    stroke(0)
    lineCap("round")
    lineDash(.25, 2.5)
    
    # Top line
    line((margin, h*0.95), (w-margin,h*0.95))
    
    # Bottom line
    line((margin, h*0.05), (w-margin,h*0.05))
    
    stroke(None)
    lineDash(None)


# Function that draws each glyph
def glyph2draw(layer, boxOrigin, boxWidth, boxHeight = 20, font = f):
    
    # Positions
    originX, originY = boxOrigin

    # Scale factor 
    scaleFactor = boxHeight/(f.masters[0].capHeight*2)
    myCapHeight = f.glyphs['H'].layers[0].bounds.size.height
    #print("Scale factor = %s" % (scaleFactor))
    #print(myCapHeight)
    
    # Colors
    fill(0)
    stroke(0)
    #strokeWidth(0)
    
    # ································· 
    # Text in each box
    # ································· 
    glyphName = FormattedString()
    glyphName.append(str(layer.parent.name), font="Barna-SemiBold", fontSize = boxHeight*.06, fill = (0))
    
    UnicodeValue = FormattedString()
    UnicodeValue.append(str(layer.parent.unicode), font="Barna-Light", fontSize = boxHeight*.06, fill = (0))
    
            

    if layer.bounds.size.width > 0 or str(layer.parent.name) == "space":
        with savedState():
            
            # Rectangle's colours
            fill(None) 
            #stroke(0)
            strokeWidth(15*scaleFactor)   
            
            # Black rectangle around     
            rect(originX, originY-boxHeight*0.2, boxWidth, boxHeight*1.2)

            # Text and glyph's color 
            fill(0.3)
            strokeWidth(15*scaleFactor)
            stroke(1)

            # Writing each text (current glyph's name and its Unicode value) 
            text(glyphName, (originX+boxWidth*.08, originY-boxHeight*.03))
            text(UnicodeValue, (originX+boxWidth*.08, originY-boxHeight*.11))
            #print(glyphName)

            
        with savedState():
            scale(scaleFactor, scaleFactor, center = (originX, originY))
            translate(originX, originY+(myCapHeight/2)) # * = unpacking tuple

            translate(
                ((boxWidth - layer.bounds.size.width * scaleFactor) / 2)/scaleFactor
                )

            # Drawing the glpyh
            drawPath(layer.completeBezierPath)
    
    # If there's an empty cell        
    else:

        # Rectangle's colours
        fill(None)
        #stroke(0)
        strokeWidth(15*scaleFactor)
        
        # Black rectangle around     
        rect(originX, originY-boxHeight*0.2, boxWidth, boxHeight*1.2)

        # Dashed lines       
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
        
        text(glyphName, (originX+boxWidth*.08, originY-boxHeight*.03))
        text(UnicodeValue, (originX+boxWidth*.08, originY-boxHeight*.11))


# ································· 
# PDF 
# ································· 

# ---------------------
# COVER

# New A4
newPage('A4')

# Unpacking its values
w, h = sizes('A4')

# Margin set to the 10% of the width
margin = w*.1

# Prints
#print("This is the width - margin", w-margin)
#print("A4 sizes", sizes('A4'))

# Background
#cmykFill(0, 90, 86, 0)
#fill(1)
#rect(0,0,w, h)


# ································· 
# Text in the cover
# ·································

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

# -----------------
# CHARACTER SET

# New A4
newPage('A4')

# Background
#cmykFill(0, 90, 86, 0)
#fill(1)
#rect(0,0,w, h)

# Columns
columns = 10
boxWidth = (w-margin*2) / columns
#print("Box widht:", boxWidth)


# ································· 
# Text in the cover
# ·································
# Typeface's name + "Character set"
generalInfo = FormattedString()
generalInfo.append("%s — Character set"%(str(f.familyName)), font="Barna-Regular", fontSize = 10, fill = (0))
text(generalInfo, (margin, h*0.96))

# Dashed lines
drawLinesTopBottom(w, h, margin)

# Point/Leading size
columnWidth = w - margin*2
print("Column width:",columnWidth)
reduc = boxWidth * 1.2
print("Reduc", reduc)
print("This is the width - margin - boxWidth", w-margin-boxWidth)

# Point sixe
size = boxWidth*.9

# Leading
leading = size*1.2


# -----------------
# Drawing the characters

# Origin positions
originX = margin 
originY = h - margin -size       

# Loop count
loop = 0

for g in exportingGlyphs:
    for m in f.masters:

        pathToDraw = g.layers[m.id]
        
        if loop == 0:

            # Function that draws the glyph
            glyph2draw(pathToDraw, (originX, originY), boxWidth, size) 
         
        else:
            
            # New page
            if originX > w-margin - reduc and originY < margin*2:
                 #print("New page needed")                 
                 loop = 0
                 
                 originX = margin
                 originY = h - margin - size 

                 # Page settings
                 newPage('A4')

                 # Background
                 #cmykFill(0, 90, 86, 0)
                 #fill(1)
                 #rect(0,0,w, h)                 

                 # Dashed lines
                 drawLinesTopBottom(w, h, margin)

                 text(generalInfo, (margin, h*0.96))
                 
                 # Function
                 glyph2draw(pathToDraw, (originX, originY), boxWidth, size)
                
                
            # New line

            elif originX >= w - margin - reduc:
                #print('originX out of the page')
                #print("Origin x out of the width:", originX)
                
                # Red guides

                #with savedState():
                #    strokeWidth(.2)
                #    stroke(1,0,0)
                #    line(
                #       (w-margin, 0),
                #       (w-margin, h)
                #       )
                            
                originX = margin
                originY = originY-leading
                translate(0, 0)
                    
                # Function
                glyph2draw(pathToDraw, (originX, originY), boxWidth, size) 
                

            else: 
                originX = originX + boxWidth

                # Function
                glyph2draw(pathToDraw, (originX, originY), boxWidth, size)

                # Blue circle (guide)
                #fill(0,0,1)
                #oval(
                #    originX-1,
                #    originY-1, 
                #    2,
                #    2)
 
        loop += 1


# ---------------------
# Telling Drawbot the drawing is done
endDrawing()

# ---------------------
# Test
# ---------------------
#print(width(), height())

# ································· 
# Saving process 
# ·································

# -----------------------------------------------------
# Accessing the directory of the file
# Setting a variable for its path
fDirectory = os.path.dirname(f.filepath) # Only the directory
fName = os.path.basename(f.filepath) # Only the name
fNameParts = os.path.splitext(fName) # Split parts
fPath = f.filepath

# -----------------------------------------------------
# Generating a text file with the report 
NewfName = fNameParts[0] + ' - Character set.pdf' # Change extension
NewfPath = os.path.join(fDirectory, NewfName) # Change extension
#print(NewfPath)

# Saving the .pdf
saveImage(NewfPath)

# ---------------------
# Test
# ---------------------
Glyphs.showNotification('Character set builder', 'Generated character set of the current font')

print("Done")

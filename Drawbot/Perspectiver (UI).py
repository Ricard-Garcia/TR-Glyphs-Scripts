# MenuTitle: Perspectiver with UI
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (@Typerepublic) - 09.12.2019 
# ------------------------------------------


__doc__="""
Deforms the current selected glyph using an affine transform matrix.
"""


# ---------------------
# Modules
# ---------------------
import vanilla


f = Glyphs.font

class perspectiveTool( object ):
    
    
    def __init__ ( self ):
        
        
        # Window sizes
        windowW, windowH = 280, 250
        
        margin = 20
        linePos = 20
        lineHeight = linePos*1.2
        
        
        self.w = vanilla.FloatingWindow(
            (windowW,windowH),
            "Perspective tool"
            )
                    
                    
        # ·····················································
        # Title
        self.w.descriptionText = vanilla.TextBox( (margin, linePos-5, -margin, lineHeight), "Select the values to apply in the current layer", sizeStyle = "small")         
        
        linePos += lineHeight   

        
        # ·····················································
        # Slider 1 (X Scale Factor)
        # Title
        self.w.xScaleTitle = vanilla.TextBox(
            (margin, linePos, -margin, lineHeight),
            "X Scale",
            sizeStyle = "small")
            
        linePos += lineHeight*.5
        # Slider
        self.w.xScale = vanilla.Slider(
            (margin, linePos, -margin, lineHeight),
            minValue = 0,
            maxValue = 1,
            value = 1,
            #tickMarkCount = 3,
            continuous = True
            )
            
        
        linePos += lineHeight   
            
            
        # ·····················································
        # Slider 2 (Y Scale Factor)
        # Title
        self.w.yScaleTitle = vanilla.TextBox(
            (margin, linePos, -margin, lineHeight),
            "Y Scale",
            sizeStyle = "small")
            
        linePos += lineHeight*.5
        # Slider
        self.w.yScale = vanilla.Slider(
            (margin, linePos, -margin, lineHeight),
            minValue = 0,
            maxValue = 1,
            value = 1,
            #tickMarkCount = 3,
            continuous = True
            )
            

        linePos += lineHeight   
            
            
        # ·····················································
        # Slider 3 (X Skew Factor)
        # Title
        self.w.xSkewTitle = vanilla.TextBox(
            (margin, linePos, -margin, lineHeight),
            "X Skew",
            sizeStyle = "small")
            
        linePos += lineHeight*.5
        # Slider
        self.w.xSkew = vanilla.Slider(
            (margin, linePos, -margin, lineHeight),
            minValue = -1,
            maxValue = 1,
            value = 0,
            #tickMarkCount = 3,
            continuous = True
            )
            

        linePos += lineHeight   
            
            
        # ·····················································
        # Slider 4 (Y Skew Factor)
        # Title
        self.w.ySkewTitle = vanilla.TextBox(
            (margin, linePos, -margin, lineHeight),
            "Y Skew",
            sizeStyle = "small")
            
        linePos += lineHeight*.5
        # Slider
        self.w.ySkew = vanilla.Slider(
            (margin, linePos, -margin, lineHeight),
            minValue = -1,
            maxValue = 1,
            value = 0,
            #tickMarkCount = 3,
            continuous = True
            )


        # ·····················································
        # Button
    
        linePos += lineHeight*1.5

        # Apply button
        self.w.applyButton = vanilla.Button(
            (margin, linePos, -margin, lineHeight),
            "Apply",
            sizeStyle = "small",
            callback = self.generatingTransformation)
        
        
        # Opening the UI window
        self.w.open()
    
    
    
    def generatingTransformation( self, sender ):
    
        # Current master ID
        masterID = f.selectedFontMaster.id

        # Get the selected layer
        layer = Glyphs.font.selectedLayers[0]
        print(layer.parent.name)
        
        layer.applyTransform([
                        self.w.xScale.get(), # x scale factor
                        self.w.xSkew.get(), # x skew factor
                        self.w.ySkew.get(), # y skew factor
                        self.w.yScale.get(), # y scale factor
                        0.0, # x position
                        0.0  # y position
                        ])
                

# Calling the object
perspectiveTool()


# ---------------------
# Test
# ---------------------
print("Done")

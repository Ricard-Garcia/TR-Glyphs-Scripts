#MenuTitle: Mark all colored marks in all opened fonts
# -*- coding: utf-8 -*-
__doc__="""
In current font, marks in color every stylistic set (until .ss03).
"""
# ----------------------------
# 14.03.2019
# ----------------------------

# Modules
from AppKit import NSColor, NSColorSpace

# Glyphs
glyphs = Font.glyphs
# Marking colors
lightBlue = NSColor.colorWithDeviceHue_saturation_brightness_alpha_(118/255, 214/255, 255/255, 1) 
midBlue = NSColor.colorWithDeviceHue_saturation_brightness_alpha_(0/255, 150/255, 255/255, 1) 
darkBlue = NSColor.colorWithDeviceHue_saturation_brightness_alpha_(0/255, 84/255, 147/255, 1)

grey = NSColor.colorWithDeviceHue_saturation_brightness_alpha_(100/255, 100/255, 100/255, 1)


# Loop through all fonts
	# Loop through all glyphs
for g in glyphs:
		# Coloring depending on its name
		if ".ss01" in g.name:
			g.colorObject = lightBlue
		elif ".ss02" in g.name:
			g.colorObject = darkBlue
		elif ".ss03" in g.name:
			g.colorObject = darkBlue

		# Alternate characters
		elif ".alt" in g.name:
			g.colorObject = grey

		# Other glyphs have no cmark color
		else:
			g.colorObject = None


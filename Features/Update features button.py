#MenuTitle: Update features window with button - 11.04.2019
# -*- coding: utf-8 -*-

# Ricard Garcia - ??.03.2019
# --------------------------


__doc__="""
Displays a window with a button that updates curren font's feautres.
"""


# ---------------------
# Modules
# ---------------------
from vanilla import *


# ---------------------
# Variables
# ---------------------
f = Glyphs.font


# ---------------------
# Engine
# ---------------------
class ButtonDemo(object):

     def __init__(self):
         self.w = Window((100, 40))
         self.w.button = Button((10, 10, -10, 20), "Update features", callback=self.buttonCallback)
         self.w.open()

     def buttonCallback(self, sender):
     	f.updateFeatures()
     	print("Features have been updated!")


ButtonDemo()


# ---------------------
# Test
# ---------------------
print("Done!")

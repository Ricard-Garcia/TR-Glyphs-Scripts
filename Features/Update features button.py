#MenuTitle: Update features window with button - 11.04.2019
# -*- coding: utf-8 -*-
__doc__="""
Displays a window with a button that updates curren font's feautres.
"""
from vanilla import *

f = Glyphs.font

class ButtonDemo(object):

     def __init__(self):
         self.w = Window((100, 40))
         self.w.button = Button((10, 10, -10, 20), "Update features", callback=self.buttonCallback)
         self.w.open()

     def buttonCallback(self, sender):
     	f.updateFeatures()
     	print("Features have been updated!")


ButtonDemo()


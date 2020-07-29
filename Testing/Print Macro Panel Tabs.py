# MenuTitle: Prints all tabs in Macro Panel
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia (with help from Georg) - ??.06.2019
# -------------------------------------------------


__doc__="""
In the Macro Panel, prints all of its tabs.
"""

# ---------------------
# Modules
# ---------------------
from AppKit import NSApp


# ---------------------
# Variables
# ---------------------
macroViewControllers = NSApp.delegate().macroPanelController().tabBarControl().tabItems()
i = 0

# ---------------------
# Engine
# ---------------------
for macroView in macroViewControllers:
	print("macro-------------------------------------------------------------", i)
	print(macroView.macroText().string())
	i += 1


# ---------------------
# Test
# ---------------------
print("Done!")

	
	
	
	
	
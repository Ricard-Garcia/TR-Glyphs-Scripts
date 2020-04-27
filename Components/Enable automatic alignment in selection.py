# MenuTitle: Guides through all alignment zones
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia - 27.04.2020 
# --------------------------


__doc__="""
Sets a global guideline in each alignment zone.
"""

# ---------------------
# Modules
# ---------------------


# ---------------------
# Variables
# ---------------------
f = Glyphs.font


# ---------------------
# Engine
# ---------------------
# For each alignment zone in the current master
for g in f.selection:
	for l in g.layers:
		if l.isMasterLayer == True:
			for c in l.components:
				c.automaticAlignment = True
			print(g.name, l.name, "----- Automatic alignment set")
		else:
			pass


# Pop-up notification
Glyphs.showNotification("Automatic alignment", "Set automatic alignment in all masters.")


# ---------------------
# Test
# ---------------------
print("Done!")
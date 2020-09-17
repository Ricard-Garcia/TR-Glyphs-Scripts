# MenuTitle: Disables automatic alignment for all selected glyphs in all masters
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia - 27.04.2020 
# --------------------------


__doc__="""
Disables automatic alignment for all selected glyphs in all masters.
"""

# ---------------------
# Variables
# ---------------------
f = Glyphs.font


# ---------------------
# Engine
# ---------------------
for g in f.selection:
	for l in g.layers:
		if l.isMasterLayer == True:
			for c in l.components:
				c.automaticAlignment = False
			print(g.name, l.name, "----- Automatic alignment disabled")
		else:
			pass


# Pop-up notification
Glyphs.showNotification("Disable automatic alignment", "Disabled automatic alignment in all masters.")


# ---------------------
# Test
# ---------------------
print("Done!")
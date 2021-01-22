# MenuTitle: Lock all global guidelines
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


# Ricard Garcia - 05.11.2018 
# --------------------------


__doc__="""
Locks all global guidelines in all masters.
"""


# ---------------------
# Variables
# ---------------------
f = Glyphs.font
masters = f.masters


# ---------------------
# Engine
# ---------------------
# Iterate through all masters
for m in masters:
	# Iterate through all guidelines in current master
	for g in m.guides:
		# Lock it
		g.locked = True
# Pop-up notification
Glyphs.showNotification("Global guidelines", "Global guidelines locked.")


# ---------------------
# Test
# ---------------------
print("Done!")
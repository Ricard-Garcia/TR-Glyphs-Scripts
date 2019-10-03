# MenuTitle: Font info data
# Ricard Garcia - 05.11.2018
# -------------------

# -*- coding: utf-8 -*-
__doc__="""
	Set font.info data to Current font.
"""

# ---------------------
# Variables
# ---------------------
# Current font
font = Glyphs.font


# ---------------------
# Engine
# ---------------------
# ------ Imprimir ------
print font.info.familyName
print font.info.styleName
print font.info.versionMajor
print font.info.versionMinor

print font.info.copyright
print font.info.trademark

# ------ Assignat ------
font.info.familyName = "Family Name"
font.info.styleName = "Style"
font.info.versionMajor = 1
font.info.versionMinor = 001
font.info.year = 2019

font.info.copyright = u"(c) Designer's name"
font.info.trademark = "Trade Mark"


# ---------------------
# Test
# ---------------------
print("Done!")

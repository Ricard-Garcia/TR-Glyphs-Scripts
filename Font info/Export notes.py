#MenuTitle: Generates a .txt file of the notes to the current path of the file.
# -*- coding: utf-8 -*-
__doc__="""
In file's path, generates a .txt file of current font's notes.
"""

# ---------------------
# Modules
from random import randint
import textwrap
import os

# ---------------------
# General variables
font = Glyphs.font
glyphs = font.glyphs

# ---------------------
# Accessing the directory of the file
# Setting a variable for its path
fDirectory = os.path.dirname(font.filepath) # Only the directory
fName = os.path.basename(font.filepath) # Only the name
fNameParts = os.path.splitext(fName) # Split parts
fPath = font.filepath

# Uncomment to print the path of the file
#print(fDirectory)
#print(fName)
#print(fPath)
# print(f"File name parts {fNameParts}.")


# ---------------------
# Generating features file
NewfName = fNameParts[0] + 'Notes.txt' # Change extension
NewfPath = os.path.join(fDirectory, NewfName) # Change extension

# Title
fontNotes = "# %s Notes\n\n" % (fNameParts[0])

# Adding the notes
for l in font.note:
	fontNotes += font.note

# Opening and writing the file
newFile = open(NewfPath, 'w')
newFile.write(fontNotes.encode('utf8'))
newFile.close()


# ---------------------
# Clear log in macro Panel (Glyphs)
Glyphs.clearLog()
#MenuTitle: Exporting features file - 19.02.2019
# -*- coding: utf-8 -*-
__doc__="""
From a given file, exports a .fea file with all of its features.
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
NewfName = fNameParts[0] + '.fea' # Change extension
NewfPath = os.path.join(fDirectory, NewfName) # Change extension

# Content of the .fea file

# Title
codeFeatures = "# %s features\n\n" % (fNameParts[0])


# Loop through classes
codeFeatures += "#Classes"

for c in font.classes:
	if c == 0:
		codeFeatures += "\n@%s = [%s]" % (c.name, c.code)	
	else:
		codeFeatures += "\n@%s = [%s]" % (c.name, c.code)	


# Loop through features
codeFeatures += "\n\n# Features"

for fea in font.features:
	# Name of the feature
	#print("\n\nfeature %s {" % (fea.name))
	codeFeatures += "\n\nfeature %s {" % (fea.name)
	# Inside of the feature
	for l in fea.code.splitlines():
		if l == 0:
			#print("\n\t%s" % (l))
			codeFeatures += "\n\t%s" % (l)
		else:
			#print("\n\t%s" % (l))
			codeFeatures += "\n\t%s" % (l)
	# Closing the feature
	#print('}')
	codeFeatures += '\n} %s' % (fea.name)

# Opening and writing the file
newFile = open(NewfPath, 'w')
newFile.write(codeFeatures)
newFile.close()


# ---------------------
# Clear log in macro Panel (Glyphs)
Glyphs.clearLog()
#MenuTitle: New tab with uppercase, small cap and lowercase
# -*- coding: utf-8 -*-
__doc__="""
Opens a new tab with the combination of uppercase, small cap and lowercase of each character.
"""

# Comparing uppercase, small caps and lowercase

base_characters = [ 
"a",
"aacute",
"abreve",
"acircumflex",
"adieresis",
"agrave",
"amacron",
"aogonek",
"aring",
"atilde",
"ae",
"b",
"c",
"cacute",
"ccaron",
"ccedilla",
"ccircumflex",
"cdotaccent",
"d",
"eth",
"dcaron",
"dcroat",
"e",
"eacute",
"ecaron",
"ecircumflex",
"edieresis",
"edotaccent",
"egrave",
"emacron",
"eogonek",
"f",
"g",
"gbreve",
"gcircumflex",
"gcommaaccent",
"gdotaccent",
"h",
"hbar",
"hcircumflex",
"i",
"idotless",
"iacute",
"icircumflex",
"idieresis",
"idotaccent",
"igrave",
"imacron",
"iogonek",
"itilde",
"j",
"jdotless",
"jcircumflex",
"k",
"kcommaaccent",
"kgreenlandic",
"l",
"lacute",
"lcaron",
"lcommaaccent",
"lslash",
"m",
"n",
"nacute",
"ncaron",
"ncommaaccent",
"eng",
"ntilde",
"o",
"oacute",
"ocircumflex",
"odieresis",
"ograve",
"ohungarumlaut",
"omacron",
"oslash",
"otilde",
"oe",
"p",
"thorn",
"q",
"r",
"racute",
"rcaron",
"rcommaaccent",
"s",
"sacute",
"scaron",
"scedilla",
"scircumflex",
"scommaaccent",
"germandbls",
"longs",
"t",
"tbar",
"tcaron",
"tcedilla",
"tcommaaccent",
"u",
"uacute",
"ubreve",
"ucircumflex",
"udieresis",
"ugrave",
"uhungarumlaut",
"umacron",
"uogonek",
"uring",
"utilde",
"v",
"w",
"wacute",
"wcircumflex",
"wdieresis",
"wgrave",
"x",
"y",
"yacute",
"ycircumflex",
"ydieresis",
"ygrave",
"z",
"zacute",
"zcaron",
"zdotaccent"
]

outputString = " "

for bc in base_characters:
	capitalized_letter = bc.capitalize()
	
	
	result =  "/%s /%s.sc /%s " % (capitalized_letter, bc, bc) 
	
	#Add new line + result to outputString
	outputString += "\n" + result 

	print(outputString)
	
Font.newTab(outputString)

	

	
	
	
	
	
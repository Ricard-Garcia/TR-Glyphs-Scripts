# MenuTitle: Set first and second tab to spacing strings
# -*- coding: utf-8 -*-

# Ricard Garcia (with special help from Gustavo Ferreira and Frederik Berlaen) - 08.04.2018
# --------------------------


__doc__="""
Creates first and second tab with spacing strings. First tab lowercase and second uppercase.
"""


# ---------------------
# Modules
# ---------------------
import textwrap
import os


# ---------------------
# Variables
# ---------------------
f = Glyphs.font
glyphs = f.glyphs
tabs = f.tabs
#tab1Text = os.path("/Applications/Glyphs/Glyphs.app/Contents/_Tab-text/tab1.txt")
#tab2Text = os.path("/Applications/Glyphs/Glyphs.app/Contents/_Tab-text/tab2.txt")


# ---------------------
# Engine
# ---------------------
tabCount = 0

if not tabs:
	f.newTab("""
			nnnnnnnnnnnnnn
			oooooooooooooo
			oonooonnooonoo
		
			annanonoaoo
			bnnbnonoboo
			cnncnonocoo
			dnndnonodoo
			ennenonoeoo
			fnnfnonofoo
			gnngnonogoo
			hnnhnonohoo
			inninonoioo
			jnnjnonojoo
			knnknonokoo
			lnnlnonoloo
			mnnmnonomoo
			nnnnnononoo
			onnononoooo
			pnnpnonopoo
			qnnqnonoqoo
			rnnrnonoroo
			snnsnonosoo
			tnntnonotoo
			unnunonouoo
			vnnvnonovoo
			wnnwnonowoo
			xnnxnonoxoo
			ynnynonoyoo
			znnznonozoo
			ænnænonoæoo
			đnnđnonođoo
			ðnnðnonoðoo
			łnnłnonołoo
			ľnnľnonoľoo
			ďnnďnonoďoo
			þnnþnonoþoo
			ßnnßnonoßoo
			""")
	f.newTab("""
			HHHHHHHHHHHHHH
			OOOOOOOOOOOOOO
			OOHOOOHHOOOHOO
			
			AHHAHOHOAOO
			BHHBHOHOBOO
			CHHCHOHOCOO
			DHHDHOHODOO
			EHHEHOHOEOO
			FHHFHOHOFOO
			GHHGHOHOGOO
			HHHHHOHOHOO
			IHHIHOHOIOO
			JHHJHOHOJOO
			KHHKHOHOKOO
			LHHLHOHOLOO
			MHHMHOHOMOO
			NHHNHOHONOO
			OHHOHOHOOOO
			PHHPHOHOPOO
			QHHQHOHOQOO
			RHHRHOHOROO
			SHHSHOHOSOO
			THHTHOHOTOO
			UHHUHOHOUOO
			VHHVHOHOVOO
			WHHWHOHOWOO
			XHHXHOHOXOO
			YHHYHOHOYOO
			ZHHZHOHOZOO
			ÆHHÆHOHOÆOO
			ÐHHÐHOHOÐOO
			ŁHHŁHOHOŁOO
			ÞHHÞHOHOÞOO
			ŊHHŊHOHOŊOO
			ØHHØHOHOØOO
			
			HAHBHCHDHEHFHGHHHIHJHKHLHMHNHOHPHQHRHSHTHUHVHWHXHYHZH
			OAOBOCODOEOFOGOHOIOJOKOLOMONOOOPOQOROSOTOUOVOWOXOYOZO
			HIHAHIHBHIHCHIHDHIHEHIHFHIHGHIHHHIHIHIHJHIHKHIHLHIHMHIH
			HIHNHIHOHIHPHIHQHIHRHIHSHIHTHIHUHIHVHIHWHIHXHIHYHIHZHIH
			
			HH0HH1HH2HH3HH4HH5HH6HH7HH8HH9HH OO0OO1OO2OO3OO4OO5OO6OO7OO8OO9OO
			00100200300400500600700800900
			11011211311411511611711811911
			220221222322422522622722822922
			330331332333433533633733833933
			440441442443444544644744844944
			550551552553554555655755855955
			660661662663664566666766866966
			880881882883884588886887888988
			990991992993994599996997899999
			""")
else:
	for tab in tabs:
		if tabCount == 0:
			tab.text = """
				nnnnnnnnnnnnnn
				oooooooooooooo
				oonooonnooonoo
			
				annanonoaoo
				bnnbnonoboo
				cnncnonocoo
				dnndnonodoo
				ennenonoeoo
				fnnfnonofoo
				gnngnonogoo
				hnnhnonohoo
				inninonoioo
				jnnjnonojoo
				knnknonokoo
				lnnlnonoloo
				mnnmnonomoo
				nnnnnononoo
				onnononoooo
				pnnpnonopoo
				qnnqnonoqoo
				rnnrnonoroo
				snnsnonosoo
				tnntnonotoo
				unnunonouoo
				vnnvnonovoo
				wnnwnonowoo
				xnnxnonoxoo
				ynnynonoyoo
				znnznonozoo
				ænnænonoæoo
				đnnđnonođoo
				ðnnðnonoðoo
				łnnłnonołoo
				ľnnľnonoľoo
				ďnnďnonoďoo
				þnnþnonoþoo
				ßnnßnonoßoo
				"""
			#newTab1 = open(tab1Text, 'r')
			#tab.text = newTab1
			print("First tab done!")
		elif tabCount == 1:
			tab.text = """
				HHHHHHHHHHHHHH
				OOOOOOOOOOOOOO
				OOHOOOHHOOOHOO
				
				AHHAHOHOAOO
				BHHBHOHOBOO
				CHHCHOHOCOO
				DHHDHOHODOO
				EHHEHOHOEOO
				FHHFHOHOFOO
				GHHGHOHOGOO
				HHHHHOHOHOO
				IHHIHOHOIOO
				JHHJHOHOJOO
				KHHKHOHOKOO
				LHHLHOHOLOO
				MHHMHOHOMOO
				NHHNHOHONOO
				OHHOHOHOOOO
				PHHPHOHOPOO
				QHHQHOHOQOO
				RHHRHOHOROO
				SHHSHOHOSOO
				THHTHOHOTOO
				UHHUHOHOUOO
				VHHVHOHOVOO
				WHHWHOHOWOO
				XHHXHOHOXOO
				YHHYHOHOYOO
				ZHHZHOHOZOO
				ÆHHÆHOHOÆOO
				ÐHHÐHOHOÐOO
				ŁHHŁHOHOŁOO
				ÞHHÞHOHOÞOO
				ŊHHŊHOHOŊOO
				ØHHØHOHOØOO
				
				HAHBHCHDHEHFHGHHHIHJHKHLHMHNHOHPHQHRHSHTHUHVHWHXHYHZH
				OAOBOCODOEOFOGOHOIOJOKOLOMONOOOPOQOROSOTOUOVOWOXOYOZO
				HIHAHIHBHIHCHIHDHIHEHIHFHIHGHIHHHIHIHIHJHIHKHIHLHIHMHIH
				HIHNHIHOHIHPHIHQHIHRHIHSHIHTHIHUHIHVHIHWHIHXHIHYHIHZHIH
				
				HH0HH1HH2HH3HH4HH5HH6HH7HH8HH9HH OO0OO1OO2OO3OO4OO5OO6OO7OO8OO9OO
				00100200300400500600700800900
				11011211311411511611711811911
				220221222322422522622722822922
				330331332333433533633733833933
				440441442443444544644744844944
				550551552553554555655755855955
				660661662663664566666766866966
				880881882883884588886887888988
				990991992993994599996997899999
				"""
			print("Second tab done!")
		else:
			tab.close()
			print("Other tabs have been closed.")
			
		tabCount += 1

# Glyphs notifications
Glyphs.showNotification("Sorted tabs", "Generated tabs with spacing strings.")


# ---------------------
# Test
# ---------------------
print("Done!")



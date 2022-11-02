#Packages;
import pydirectinput

#Remove delay for pydirectinput;
pydirectinput.PAUSE = 0.05 #Default is 0.05
pydirectinput.FAILSAFE = False

#Autocombo;
def autocombo():
	pydirectinput.press('1')
	pydirectinput.press('2')
	pydirectinput.press('3')
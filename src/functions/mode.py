#Packages;
import pyautogui
import pydirectinput

#Fuctions;
from src.functions.auto.autopotion import autopotion
from src.functions.auto.autocombo import autocombo
from src.functions.auto.ctrl import ctrl
from src.functions.auto.autoall import autoall
from src.functions.keys.quit import quit

#Config;
from src.functions.config.config import config

#Select Mode;
def select(mode):

	#-- AUTO POTION --#

	if mode == "1":
		print(f"""Auto potion está ligado! \nCaso queira desligar aperte {config()['config']['exit']}""")
		while True:
			pydirectinput.PAUSE = 0.1
			pydirectinput.FAILSAFE = False
			w = pyautogui.getActiveWindowTitle()
			if w == f"""{config()['config']['name']}""":
				autopotion()
				quit()
			else:
				quit()


	#-- AUTO COMBO (BLADE MASTER) --#

	if mode == "2":
		print(f"""Auto combo está ligado! \nCaso queira desligar aperte {config()['config']['exit']}""")
		while True:
			w = pyautogui.getActiveWindowTitle()
			if w == f"""{config()['config']['name']}""":
				autocombo()
				quit()
			else:
				quit()

	#-- AUTO CTRL --#

	if mode == "3":
		print(f"""CTRL está ligado! \nCaso queira desligar aperte {config()['config']['exit']}""")
		while True:
			pydirectinput.PAUSE = 0.1
			pydirectinput.FAILSAFE = False
			w = pyautogui.getActiveWindowTitle()
			if w == f"""{config()['config']['name']}""":
				ctrl()
				quit()
			else:
				quit()

	#-- ALL FUNCTIONS --#

	if mode == "10":
		print(f"""Todas as funções foram ativadas com sucesso! \nCaso queirar finalizar elas aperte {config()['config']['exit']}""")
		while True:
			pydirectinput.PAUSE = 0.1
			pydirectinput.FAILSAFE = False
			w = pyautogui.getActiveWindowTitle()
			if w == f"""{config()['config']['name']}""":
				autoall()
				quit()
			else:
				quit()
#Packages;
import keyboard

#Config;
from src.functions.config.config import config

#Quit;
def quit():
	if keyboard.is_pressed(config()['config']['exit']):
		exit()
#Functions;
from src.functions.mode import select

#Start;
def start(mode):

	#Verificar se é um número;
	if mode.isnumeric() == False:
		print(f"""\n{mode} não é uma função válida. \nO sistema será finalizado.""")
		exit()

	#Funções válidas;
	check = ['1', '2', '3', '10']

	#Loop;
	for i in check:
		if i == mode:
			select(mode)
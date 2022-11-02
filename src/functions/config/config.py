#Packages;
import yaml

#Config;
def config():
	try:
		with open("config.yml", encoding="utf8") as file:
			config = yaml.safe_load(file)
			#print('|----> Configurações (config.yml) foi carregado com sucesso!')
			return config
	except:
		print('[Sistema] - O arquivo de configurações (config.yml) não foi encontrado.')
		print('[Sistema] - O Macro está sendo encerrado.')
		exit()
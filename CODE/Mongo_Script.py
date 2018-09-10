import pymongo
from pymongo import MongoClient

class DAO_MONGO ():
	def __init__(self):

		cliente =  MongoClient('localhost', 27017)
		db = cliente['DOCS']

		self.DOC_Prontuarios = db['prontuarios']
		self.DOC_Doenca = db['doencas']

	def Novo_Prontuario (self, ID_Prontuario, Doenca = '', Sintomas = [], Sinais = []):
		self.DOC_Prontuarios.insert({
				'ID_Prontuario' : ID_Prontuario,
				'Doenca' : Doenca,
				'Sintomas' : Sintomas,
				'Sinais' : Sinais
			})

	def Nova_Doenca (sef, Nome, Sinais_Clinicos = []):
		self.DOC_Doenca.insert({
			'Nome' : Nome,
			'Sinais_Clinicos' : Sinais_Clinicos
			})

	def Doenca_por_Sintomas_Sinais (self, Sintomas = [], Sinais = []):
		dado = self.DOC_Doenca.find({'&and' : [{'Sinais_Clinicos' : {'$all' : Sintomas}}, {'Sinais_Clinicos' : {'$all' : Sinais}}]}, {'_id' : False})
		return dado
		
	def Prontuario_por_Doenca (self, Doenca = ''):
		dado = self.DOC_Prontuarios.find({'Doenca' : Doenca}, {'_id' : False})
		return dado

	def Prontuario_por_Sintomas (self, Sintomas = []):
		dado = self.DOC_Prontuarios.find({'Sintomas' : {'$all' : Sintomas}}, {'_id' : False})
		return 

	def Prontuario_por_Sinais (self, Sinais = []):
		dado = self.DOC_Prontuarios.find({'Sinais' : {'$all' : Sinais}}, {'_id' : False})
		return dado

	def Prontuario_por_Sintomas_Sinais (self, Sintomas = [], Sinais = []):
		dado = self.DOC_Prontuarios.find( {'$and' : [{'Sinais' : {'$all' : Sinais}}, {'Sintomas' : {'$all' : Sintomas}}]}, {'_id' : False})
		return dado


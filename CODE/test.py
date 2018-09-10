
#iniciar servidor
#mongod --dbpath C:/MongoDB/MongoData
#--------------------------------
'''
import pymongo
from pymongo import MongoClient

#conecta ao server do mongo
cliente = MongoClient('localhost', 27017)

#define o banco de dados
db = cliente['teste']


#cria o documento
tabela = db['estudo']


#insere no documento
tabela.insert({
	'nome':'gabriel',
	'idade':'22'
	})

#ou pode usar a forma compacta
db.testando.insert({'nome':'gabriel','idade':'22'})

#tras todos os itens dentro do documento
x = db.testando.find()

for i in x:
	print i
'''

from Mongo_Script import DAO_MONGO
from SQL_Script import DAO_SQL
from Model import Model
from API_Script import API

model = Model()

#model.novo_medico('xxx', 111)
#dados = model.busca_medico_crm (111)

#for i in dados:
#	print i
'''
x = model.prontuario_por_sintomas_sinais(['teste'],[''])
for i in x:
	print i
'''

'''
model.novo_paciente('gabriel candeas',43550527888,23,434407562,'brasil','sao paulo','tremembe','parque das fontes','rua mambore',45,12120000)
model.novo_paciente('elaine cristina',43650527888,23,434407562,'brasil','sao paulo','tremembe','centro','nossa senhora da gloria',58,12120000)
model.novo_paciente('marcio alves',43750527888,23,434407562,'brasil','sao paulo','tremembe','parque nossa senhora da gloria','rua roseira',140,12120000)
model.novo_paciente('cristiane uchimura',43850527888,23,434407562,'brasil','sao paulo','tremembe','parque das fontes','rua aguas de sao pedro',155,12120000)


model.novo_atendente('neide candeas', 434407562, 43550527888)

model.novo_enfermeiro('paulo santos', 123456)
model.novo_medico('pedro pascoli', 1234)

model.novo_prontuario('120/80', 36.5, 'dengue', 1, 1, 1, 1)
model.novo_prontuario('120/80', 36.5, 'dengue', 2, 1, 1, 1)
model.novo_prontuario('120/80', 36.5, 'zika', 3, 1, 1, 1)
model.novo_prontuario('120/80', 36.5, 'febre amarela', 4, 1, 1, 1)
'''


#model.novo_doc_prontuario(1)
#print model.indicador_por_sintomas_sinais(['teste'],['teste1'])

'''

'''


#model.novo_atendente('nome', 111, 111)

#model.novo_doc_prontuario(222,'teste' ,['teste','teste'],['teste','teste'])
#model.novo_doc_prontuario(222,'teste1' ,['teste','teste'],['teste','teste'])
'''
x = MONGO.DOC_Prontuarios.find()

for i in x:
	print i['ID_Prontuario']

'''

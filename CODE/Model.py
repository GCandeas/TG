from SQL_Script import DAO_SQL
from Mongo_Script import DAO_MONGO
from API_Script import API

class Model ():
	def __init__ (self):
		self.sql = DAO_SQL ()
		self.mongo = DAO_MONGO ()
		self.api = API ()
		self.ambiente = {'atendente':'', 'paciente':'', 'infermeiro':'', 'medico':'', 'fila_triagem':[], 'fila_atendimento':[]}

	def novo_paciente (self, nome, cpf, idade, rg, pais, estado, cidade, bairro, rua, numero, cep):
		coordenadas = self.api.Coordenada_por_Endereco ([pais, estado, cidade, bairro, rua, numero])
		self.sql.Conecta ()
		self.sql.Paciente_Novo (nome, cpf, idade, rg, pais, estado, cidade, bairro, rua, numero, cep, coordenadas[0], coordenadas[1])
		self.sql.Fecha ()

	def novo_atendente (self, nome, rg, cpf):
		self.sql.Conecta ()
		self.sql.Atendente_Novo (nome, rg, cpf)
		self.sql.Fecha ()

	def novo_enfermeiro (self, nome, coren):
		self.sql.Conecta ()
		self.sql.Enfermeiro_Novo (nome, coren)
		self.sql.Fecha ()

	def novo_medico (self, nome, crm):
		self.sql.Conecta ()
		self.sql.Medico_Novo (nome, crm)
		self.sql.Fecha ()

	def novo_prontuario (self, id_paciente, id_atendente, pa = '', temperatura = 0, doenca = '', id_enfermeiro = 1, id_medico = 1):
		self.sql.Conecta ()
		self.sql.Prontuario_Novo (pa, temperatura, doenca, id_paciente, id_atendente, id_enfermeiro, id_medico)
		self.sql.Fecha ()

	def novo_sinal (self, sinal, id_prontuario):
		self.sql.Conecta ()
		self.sql.Sinal_Novo (sinal, id_prontuario)
		self.sql.Fecha ()

	def novo_sintoma (self, sintoma, id_prontuario):
		self.sql.Conecta ()
		self.sql.Sintoma_Novo (sintoma, id_prontuario)
		self.sql.Fecha ()

#-----------------------------------------------------------------------------------------------------------------

	def atualiza_prontuario_pa (self, id_prontuario, pa):
		self.sql.Conecta ()
		self.sql.Prontuario_Update_PA (id_prontuario, pa)
		self.sql.Fecha ()

	def atualiza_prontuario_temperatura (self, id_prontuario, temperatura):
		self.sql.Conecta ()
		self.sql.Prontuario_Update_Temperatura (id_prontuario, temperatura)
		self.sql.Fecha ()

	def atualiza_prontuario_doenca (self, id_prontuario, doenca):
		self.sql.Conecta ()
		self.sql.Prontuario_Update_Doenca (id_prontuario, doenca)
		self.sql.Fecha ()

	def atualiza_prontuario_Enfermeiro (self, id_prontuario, id_enfermeiro):
		self.sql.Conecta ()
		self.sql.Prontuario_Update_Enfermeiro (id_prontuario, id_enfermeiro)
		self.sql.Fecha ()

	def atualiza_prontuario_medico (self, id_prontuario, id_medico):
		self.sql.Conecta ()
		self.sql.Prontuario_Update_Medico (id_prontuario, id_medico)
		self.sql.Fecha ()

	def atualiza_paciente_estado (self, id_paciente, estado):
		self.sql.Conecta ()
		self.sql.Paciente_Update_Estado (id_paciente, estado)
		self.sql.Fecha ()

	def atualiza_paciente_cidade (self, id_paciente, cidade):
		self.sql.Conecta ()
		self.sql.Paciente_Update_Cidade (id_paciente, cidade)
		self.sql.Fecha ()

	def atualiza_paciente_bairro (self, id_paciente, bairro):
		self.sql.Conecta ()
		self.sql.Paciente_Update_Bairro (id_paciente, bairro)
		self.sql.Fecha ()

	def atualiza_paciente_rua (self, id_paciente, rua):
		self.sql.Conecta ()
		self.sql.Paciente_Update_Rua (id_paciente, rua)
		self.sql.Fecha ()

	def atualiza_paciente_numero (self, id_paciente, numero):
		self.sql.Conecta ()
		self.sql.Paciente_Update_Numero (id_paciente, numero)
		self.sql.Fecha ()

	def atualiza_paciente_cep (self, id_paciente, cep):
		self.sql.Conecta ()
		self.sql.Paciente_Update_CEP (id_paciente, cep)
		self.sql.Fecha ()

#----------------------------------------------------------------------------------------------------

	def busca_medico_crm (self, crm):
		self.sql.Conecta ()
		dados = self.sql.Medico_Consulta_CRM (crm)
		self.sql.Fecha ()
		return dados

	def busca_infermeiro_coren (self, coren):
		self.sql.Conecta ()
		dados = self.sql.Enfermeiro_Consulta_COREN (coren)
		self.sql.Fecha ()
		return dados

	def busca_atendente_cpf (self, cpf):
		self.sql.Conecta ()
		dados = self.sql.Atendente_Consulta_CPF (cpf)
		self.sql.Fecha ()
		return dados

	def busca_paciente_cpf (self, cpf):
		self.sql.Conecta ()
		dados = self.sql.Paciente_Consulta_CPF (cpf)
		self.sql.Fecha ()
		return dados

	def busca_paciente_rg (self, rg):
		self.sql.Conecta ()
		dados = self.sql.Paciente_Consulta_RG (rg)
		self.sql.Fecha ()
		return dados

	def busca_paciente_idpaciente (self, num_id):
		self.sql.Conecta ()
		dados = self.sql.Paciente_Consulta_IDPaciente (num_id)
		self.sql.Fecha ()
		return dados

	def busca_prontuario_idprontuario (self, num_id):
		self.sql.Conecta ()
		dados = self.sql.Prontuario_Consulta_IDProntuario (num_id)
		self.sql.Fecha ()
		return dados

	def busca_prontuario_idpaciente (self, num_id):
		self.sql.Conecta ()
		dados = self.sql.Prontuario_Consulta_IDPaciente (num_id)
		self.sql.Fecha ()
		return dados

	def busca_prontuario_doenca (self, doenca):
		self.sql.Conecta ()
		dados = self.sql.Prontuario_Consulta_Doenca (doenca)
		self.sql.Fecha ()
		return dados

	def busca_sinais_idprontuario (self, num_id):
		self.sql.Conecta ()
		dados = self.sql.Sinais_Consulta_IDProntuario (num_id)
		self.sql.Fecha ()
		return dados

	def busca_sintomas_idprontuario (self, num_id):
		self.sql.Conecta ()
		dados = self.sql.Sintomas_Consulta_IDProntuario (num_id)
		self.sql.Fecha ()
		return dados

#------------------------------------------------------------------------------------------------------------------------
	def ambiente_atendente (self, atendente = []):
		self.ambiente['atendente'] = {
		'id':atendente[0], 
		'nome':atendente[1],
		'rg':atendente[2], 
		'cpf':atendente[3], 
		}

	def ambiente_paciente (self, paciente = []):
		self.ambiente['paciente'] = {
		'id':paciente[0], 
		'nome':paciente[1], 
		' cpf':paciente[2], 
		'idade':paciente[3], 
		'rg':paciente[4], 
		'pais':paciente[5], 
		'estado':paciente[6], 
		'cidade':paciente[7], 
		'bairro':paciente[8], 
		'rua':paciente[9], 
		'numero':paciente[10], 
		'cep':paciente[11]
		}

	def ambiente_infermeiro (self, infermeiro = []):
		self.ambiente['infermeiro'] = {
		'id':infermeiro[0], 
		'nome':infermeiro[1],
		'coren':infermeiro[2], 
		}

	def ambiente_medico (self, medico = []):
		self.ambiente['medico'] = {
		'id':medico[0], 
		'nome':medico[1],
		'crm':medico[2], 
		}

#------------------------------------------------------------------------------------------------------------------------	

	#arumar para q a pesquisa seja automatica
	def novo_doc_prontuario (self, id_prontuario):
		prontuario = self.busca_prontuario_idprontuario (id_prontuario)
		sintomas = self.busca_sintomas_idprontuario (id_prontuario)
		sinais = self.busca_sinais_idprontuario (id_prontuario)
		aux = []
		for i in sintomas:
			aux.append(i[0][0])

		sintomas = aux
		aux = []
		for i in sinais:
			aux.append(i[0][0])

		sinais = aux
		self.mongo.Novo_Prontuario (id_prontuario, prontuario[3], sintomas, sinais)

	def novo_doc_doenca (self, nome, sinais_clinicos):
		self.mongo.Nova_Doenca (nome, sinais_clinicos)

	def doenca_por_sinais_clinicos (self, sintomas = [], sinais = []):
		dados = self.mongo.Doenca_por_Sinais_Clinicos (sintomas, sinais)
		return dados

	def prontuario_por_doenca (self, doenca):
		dados = self.mongo.Prontuario_por_Doenca (doenca)
		return dados

	def prontuario_por_sintomas (self, sintomas = []):
		dados = self.mongo.Prontuario_por_Sintomas (sintomas)
		return dados

	def prontuario_por_sinais (self, sinais = []):
		dados = self.mongo.Prontuario_por_Sinais (sinais)
		return dados

	def prontuario_por_sintomas_sinais (self, sintomas = [], sinais = []):
		dados = self.mongo.Prontuario_por_Sintomas_Sinais (sintomas, sinais)
		return dados

#-------------------------------------------------------------------------------------------------------------------------
	def lat_lng_por_doenca (self, doenca):
		prontuarios = self.busca_prontuario_doenca (doenca)
		pacientes = []
		dados = []
		for i in prontuarios:
			pacientes.append(self.busca_paciente_idpaciente(i[0]))

		for i in pacientes:
			dados.append([i[0][12], i[0][13]])

		return dados

	def indicador_por_sinais (self, sinais = []):
		prontuarios = self.prontuario_por_sinais (sinais)
		num_total_ocorrencia = 0
		dados = {}
		for i in prontuarios:
			num_total_ocorrencia += 1.00
			if i['Doenca'] in dados:
				dados[i['Doenca']] += 1
			else:
				dados[i['Doenca']] = 1

		for i in dados.keys():
			if num_total_ocorrencia != 0:
				porcentagem = (dados[i] / num_total_ocorrencia) * 100
			else:
				porcentagem = 0
			dados[i] = porcentagem
		
		if not dados:
			return 0
		else:
			return dados

	def indicador_por_sintomas (self, sintomas = []):
		prontuarios = self.prontuario_por_sintomas (sintomas)
		num_total_ocorrencia = 0
		dados = {}
		for i in prontuarios:
			num_total_ocorrencia += 1.00
			if i['Doenca'] in dados:
				dados[i['Doenca']] += 1
			else:
				dados[i['Doenca']] = 1

		for i in dados.keys():
			if num_total_ocorrencia != 0:
				porcentagem = (dados[i] / num_total_ocorrencia) * 100
			else:
				porcentagem = 0
			dados[i] = porcentagem
		
		if not dados:
			return 0
		else:
			return dados

	def indicador_por_sintomas_sinais (self, sintomas = [], sinais = []):
		prontuarios = self.prontuario_por_sintomas_sinais (sintomas, sinais)
		num_total_ocorrencia = 0
		dados = {}
		for i in prontuarios:
			num_total_ocorrencia += 1.00
			if i['Doenca'] in dados:
				dados[i['Doenca']] += 1
			else:
				dados[i['Doenca']] = 1

		for i in dados.keys():
			if num_total_ocorrencia != 0:
				porcentagem = (dados[i] / num_total_ocorrencia) * 100
			else:
				porcentagem = 0
			dados[i] = porcentagem
		
		if not dados:
			return 0
		else:
			return dados


	
from Model import Model
from bottle import route, run, template, post, request, static_file

model = Model()

class Controle():
	@route ('<path:path>')
	def server_static(path):
		return static_file(path, root='VIEWS/') 
	
	@route ('/main')
	def main ():
		return template('VIEWS/main.tpl')

	@post ('/direciona')
	def encaminha ():
		cargo = request.forms.get('cargo')
		documento = int(request.forms.get('id'))

		if cargo == 'atendente':
			usuario = model.busca_atendente_cpf(documento)
			if usuario:
				model.ambiente_atendente(usuario[0])
				return template('VIEWS/atendimento.tpl', busca = 'Digite o CPF', nome = '', idade = '', rg = '', cpf = '', pais = '', estado = '', cidade = '', bairro = '', rua = '', numero = '', cep = '')

		elif cargo == 'infermeiro':
			usuario = model.busca_infermeiro_coren(documento)
			if usuario:
				model.ambiente_infermeiro(usuario[0])
				return template('VIEWS/triagem.tpl')

		elif cargo == 'medico':
			usuario = model.busca_medico_crm(documento)
			if usuario:
				model.ambiente_medico(usuario[0])
				return template('VIEWS/consulta.tpl')
		
		return template('VIEWS/main.tpl')


	@post ('/procura_paciente')
	def procura_paciente ():
		cpf = request.forms.get('busca_cpf')
		try:
			paciente = model.busca_paciente_cpf(cpf)
			model.ambiente_paciente(paciente[0])

		except:
			return template('VIEWS/atendimento.tpl', busca = 'Valor de CPF Invalido', nome = '', idade = '', rg = '', cpf = '', pais = '', estado = '', cidade = '', bairro = '', rua = '', numero = '', cep = '')

		if paciente:
			return template('VIEWS/atendimento.tpl', busca = 'Paciente Encontrado', nome = paciente[0][1], idade = paciente[0][3], rg = paciente[0][4], cpf = paciente[0][2], pais = paciente[0][5], estado = paciente[0][6], cidade = paciente[0][7], bairro = paciente[0][8], rua = paciente[0][9], numero = paciente[0][10], cep = paciente[0][11])

		else:
			return template('VIEWS/atendimento.tpl', busca = 'Paciente Nao Encontrado, Digite o CPF', nome = '', idade = '', rg = '', cpf = '', pais = '', estado = '', cidade = '', bairro = '', rua = '', numero = '', cep = '')

	@post ('/novo_paciente')
	def novo_paciente ():
		nome = request.forms.get('nome') 
		cpf = request.forms.get('cpf')
		idade = request.forms.get('idade')
		rg = request.forms.get('rg')
		pais = request.forms.get('pais')
		estado = request.forms.get('estado')
		cidade = request.forms.get('cidade')
		bairro = request.forms.get('bairro')
		rua = request.forms.get('rua')
		numero = request.forms.get('numero')
		cep = request.forms.get('cep')
		paciente = model.busca_paciente_cpf(cpf)
		model.ambiente_paciente(paciente[0])
		if paciente:
			return template('VIEWS/atendimento.tpl', busca = 'Paciente ja Cadastrado', nome = paciente[0][1], idade = paciente[0][3], rg = paciente[0][4], cpf = paciente[0][2], pais = paciente[0][5], estado = paciente[0][6], cidade = paciente[0][7], bairro = paciente[0][8], rua = paciente[0][9], numero = paciente[0][10], cep = paciente[0][11])
		
		else:
			model.novo_paciente(nome, cpf, idade, rg, pais, estado, cidade, bairro, rua, numero, cep)
			paciente = model.busca_paciente_cpf(cpf)
			model.ambiente_paciente(paciente[0])
			return template('VIEWS/atendimento.tpl', busca = 'Paciente Cadastrado com Exito', nome = paciente[0][1], idade = paciente[0][3], rg = paciente[0][4], cpf = paciente[0][2], pais = paciente[0][5], estado = paciente[0][6], cidade = paciente[0][7], bairro = paciente[0][8], rua = paciente[0][9], numero = paciente[0][10], cep = paciente[0][11])

	@post ('/atualiza_paciente')
	def atualiza_paciente ():
		cpf = request.forms.get('cpf')
		estado = request.forms.get('estado')
		cidade = request.forms.get('cidade')
		bairro = request.forms.get('bairro')
		rua = request.forms.get('rua')
		numero = request.forms.get('numero')
		cep = request.forms.get('cep')
		paciente = model.busca_paciente_cpf(cpf)
		if paciente:
			model.atualiza_paciente_estado(paciente[0][0], estado)
			model.atualiza_paciente_cidade(paciente[0][0], cidade)
			model.atualiza_paciente_bairro(paciente[0][0], bairro)
			model.atualiza_paciente_rua(paciente[0][0], rua)
			model.atualiza_paciente_numero(paciente[0][0], numero)
			model.atualiza_paciente_cep(paciente[0][0], cep)
			paciente = model.busca_paciente_cpf(cpf)
			model.ambiente_paciente(paciente[0])
			return template('VIEWS/atendimento.tpl', busca = 'Paciente Atualizado', nome = paciente[0][1], idade = paciente[0][3], rg = paciente[0][4], cpf = paciente[0][2], pais = paciente[0][5], estado = paciente[0][6], cidade = paciente[0][7], bairro = paciente[0][8], rua = paciente[0][9], numero = paciente[0][10], cep = paciente[0][11])
		
		else:
			return template('VIEWS/atendimento.tpl', busca = 'Paciente Nao Encontrado, Digite o CPF', nome = '', idade = '', rg = '', cpf = '', pais = '', estado = '', cidade = '', bairro = '', rua = '', numero = '', cep = '')
		
	@post ('/encaminha_paciente')
	def encaminha_paciente ():
		cpf = request.forms.get('cpf')
		paciente = model.busca_paciente_cpf(cpf)
		if paciente:
			model.ambiente_paciente(paciente[0])
			model.novo_prontuario(model.ambiente['paciente']['id'], model.ambiente['atendente']['id'])
			prontuario = model.busca_prontuario_idpaciente(model.ambiente['paciente']['id'])
			model.ambiente['fila_triagem'].append(prontuario[-1])

		return template('VIEWS/atendimento.tpl', busca = 'Paciente Encaminhado, Digite o CPF', nome = '', idade = '', rg = '', cpf = '', pais = '', estado = '', cidade = '', bairro = '', rua = '', numero = '', cep = '')
		
	


	if __name__ == '__main__':
		#host='0.0.0.0'
		run(host='localhost', port=8080)

#trabalhar na tela de triagem, tela de atendimento e tela do mapap e tela do adm
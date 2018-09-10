import mysql.connector

class DAO_SQL ():
	def __init__ (self):
		self.Servidor = 'localhost'
		self.Usuario = 'root'
		self.Senha = 'admin'
		self.Banco = 'tcc'
		self.Cursor = None
		self.BD = None

	def Conecta (self):
		self.BD = mysql.connector.connect (user = self.Usuario, password = self.Senha, host = self.Servidor, database = self.Banco)
		self.Cursor = self.BD.cursor()

	def Fecha (self):
		self.BD.close()

	def Paciente_Novo (self, nome, cpf, idade, rg, pais, estado, cidade, bairro, rua, numero, cep, lat, lng):
		try:
			self.Cursor.execute("INSERT INTO Paciente (Nome, CPF, Idade, RG, Pais, Estado, Cidade, Bairro, Rua, Numero, CEP, LAT, LNG) VALUES ('" + nome + "', " + str(cpf) + ", " + str(idade) + ", " + str(rg) + ", '" + pais + "', '" + estado + "', '" + cidade + "', '" + bairro + "', '" + rua + "', " + str(numero) + ", " + str(cep) + ", " + str(lat) + ", " + str(lng) + ")")
			self.BD.commit()
		except:
			self.BD.rollback()

	def Atendente_Novo (self, nome, rg, cpf):
		try:
			self.Cursor.execute("INSERT INTO Atendente (Nome, RG, CPF) VALUES ('" + nome + "', " + str(rg) + ", " + str(cpf) + ")")
			self.BD.commit()
		except:
			print 'fora'
			self.BD.rollback()

	def Enfermeiro_Novo (self, nome, coren):
		try:
			self.Cursor.execute("INSERT INTO Enfermeiro (Nome, COREN) VALUES ('" + nome + "', " + str(coren) + ")")
			self.BD.commit()
		except:
			self.rollback()

	def Medico_Novo (self, nome, crm):
		try:
			self.Cursor.execute("INSERT INTO Medico (Nome, CRM) VALUES ('" + nome + "', " + str(crm) + ")")
			self.BD.commit()
		except:
			self.rollback()

	def Prontuario_Novo (self, pa, temperatura, doenca, id_paciente, id_atendente, id_enfermeiro, id_medico):
		try:
			self.Cursor.execute("INSERT INTO Prontuario (Pressao_Arterial, Temperatura, Doenca, ID_Paciente, ID_Atendente, ID_Enfermeiro, ID_Medico) VALUES ('" + pa + "', " + str(temperatura) + ", '" + doenca + "', " + str(id_paciente) + ", " + str(id_atendente) + ", " + str(id_enfermeiro) + ", " + str(id_medico) + ")")
			self.BD.commit()
		except:
			print 'fora'
			self.BD.rollback()

	def Sinal_Novo (self, sinal, id_prontuario):
		try:
			self.Cursor.execute("INSERT INTO Sinais (Sinal, ID_Prontuario) VALUES ('" + sinal + "', " + str(id_prontuario) + ")")
			self.BD.commit()
		except:
			self.BD.rollback()

	def Sintoma_Novo (self, sintoma, id_prontuario):
		try:
			self.Cursor.execute("INSERT INTO Sintoma (Sintoma, ID_Prontuario) VALUES ('" + sintoma + "', " + str(id_prontuario) + ")")
			self.BD.commit()
		except:
			self.BD.rollback()

	#--------------------------------------------------------------------------------------------------------------------------------------

	def Prontuario_Update_PA (self, id_prontuario, pa):
		try:
			self.Cursor.execute("UPDATE Prontuario SET Pressao_Arterial = '" + pa + "' WHERE ID_Prontuario = " + str(id_prontuario))
			self.BD.commit()
		except:
			self.BD.rollback()

	def Prontuario_Update_Temperatura (self, id_prontuario, temperatura):
		try:
			self.Cursor.execute("UPDATE Prontuario SET Temperatura = " + str(temperatura) + "WHERE ID_Prontuario = " + str(id_prontuario))
			self.BD.commit()
		except:
			self.BD.rollback()

	def Prontuario_Update_Doenca (self, id_prontuario, doenca):
		try:
			self.Cursor.execute("UPDATE Prontuario SET Doenca = '" + doenca + "' WHERE ID_Prontuario = " + str(id_prontuario))
			self.BD.commit()
		except:
			self.BD.rollback()

	def Prontuario_Update_Enfermeiro (self, id_prontuario, id_enfermeiro):
		try:
			self.Cursor.execute("UPDATE Prontuario SET ID_Enfermeiro = " + str(id_enfermeiro) + "WHERE ID_Prontuario = " + str(id_prontuario))
			self.BD.commit()
		except:
			self.BD.rollback()

	def Prontuario_Update_Medico (self, id_prontuario, id_medico):
		try:
			self.Cursor.execute("UPDATE Prontuario SET ID_Medico = " + str(id_medico) + "WHERE ID_Prontuario = " + str(id_prontuario))
			self.BD.commit()
		except:
			self.BD.rollback()

	def Paciente_Update_Estado (self, id_paciente, estado):
		try:
			self.Cursor.execute("UPDATE Paciente SET Estado = '" + estado + "' WHERE ID_Paciente = " + str(id_paciente))
			self.BD.commit()
		except:
			self.BD.rollback()

	def Paciente_Update_Cidade (self, id_paciente, cidade):
		try:
			self.Cursor.execute("UPDATE Paciente SET Cidade = '" + cidade + "' WHERE ID_Paciente = " + str(id_paciente))
			self.BD.commit()
		except:
			self.BD.rollback()

	def Paciente_Update_Bairro (self, id_paciente, bairro):
		try:
			self.Cursor.execute("UPDATE Paciente SET Bairro = '" + bairro + "' WHERE ID_Paciente = " + str(id_paciente))
			self.BD.commit()
		except:
			self.BD.rollback()

	def Paciente_Update_Rua (self, id_paciente, rua):
		try:
			self.Cursor.execute("UPDATE Paciente SET Rua = '" + rua + "' WHERE ID_Paciente = " + str(id_paciente))
			self.BD.commit()
		except:
			self.BD.rollback()

	def Paciente_Update_Numero (self, id_paciente, numero):
		try:
			self.Cursor.execute("UPDATE Paciente SET Numero = " + str(numero) + " WHERE ID_Paciente = " + str(id_paciente))
			self.BD.commit()
		except:
			self.BD.rollback()

	def Paciente_Update_CEP (self, id_paciente, cep):
		try:
			self.Cursor.execute("UPDATE Paciente SET CEP = " + str(cep) + " WHERE ID_Paciente = " + str(id_paciente))
			self.BD.commit()
		except:
			self.BD.rollback()

	#--------------------------------------------------------------------------------------------------------------------------------------
	
	def Medico_Consulta_CRM (self, crm):
		try:
			self.Cursor.execute("SELECT * FROM Medico WHERE CRM = " + str(crm))
			results = self.Cursor.fetchall()
			return results
		except:
			return 0
	
	def Enfermeiro_Consulta_COREN (self, coren):
		try:
			self.Cursor.execute("SELECT * FROM Enfermeiro WHERE COREN = " + str(coren))
			results = self.Cursor.fetchall()
			return results
		except:
			return 0

	def Atendente_Consulta_CPF (self, cpf):
		try:
			self.Cursor.execute("SELECT * FROM Atendente WHERE CPF = " + str(cpf))
			results = self.Cursor.fetchall()
			return results
		except:
			return 0
	
	def Paciente_Consulta_CPF (self, cpf):
		try:
			self.Cursor.execute("SELECT * FROM Paciente WHERE CPF = " + str(cpf))
			results = self.Cursor.fetchall()
			return results
		except:
			return 0

	def Paciente_Consulta_RG (self, rg):
		try:
			self.Cursor.execute("SELECT * FROM Paciente WHERE RG = " + str(rg))
			results = self.Cursor.fetchall()
			return results
		except:
			return 0

	def Paciente_Consulta_IDPaciente (self, id_paciente):
		try:
			self.Cursor.execute("SELECT * FROM Paciente WHERE ID_Paciente = " + str(id_paciente))
			results = self.Cursor.fetchall()
			return results
		except:
			return 0

	def Paciente_Consulta_Nome (self, nome):
		try:
			self.Cursor.execute("SELECT * FROM Paciente WHERE Nome = '" + nome + "'")
			results = self.Cursor.fetchall()
			return results
		except:
			return 0

	def Prontuario_Consulta_IDProntuario (self, id_prontuario):
		try:
			self.Cursor.execute("SELECT * FROM Prontuario WHERE ID_Prontuario = " + str(id_prontuario))
			results = self.Cursor.fetchall()
			return results
		except:
			return 0

	def Prontuario_Consulta_IDPaciente (self, id_paciente):
		try:
			self.Cursor.execute("SELECT * FROM Prontuario WHERE ID_Paciente = " + str(id_paciente))
			results = self.Cursor.fetchall()
			return results
		except:
			return 0

	def Prontuario_Consulta_Doenca (self, doenca):
		try:
			self.Cursor.execute("SELECT * FROM Prontuario WHERE Doenca = '" + doenca + "'")
			results = self.Cursor.fetchall()
			return results
		except:
			return 0

	def Sinais_Consulta_IDProntuario (self, id_prontuario):
		try:
			self.Cursor.execute("SELECT * FROM Sinais WHERE ID_Prontuario = " + str(id_prontuario))
			results = self.Cursor.fetchall()
			return results
		except:
			return 0

	def Sintomas_Consulta_IDProntuario (self, id_prontuario):
		try:
			self.Cursor.execute("SELECT * FROM Sintomas WHERE ID_Prontuario = " + str(id_prontuario))
			results = self.Cursor.fetchall()
			return results
		except:
			return 0
#---------------------------------------------------------------------------------------------------

	
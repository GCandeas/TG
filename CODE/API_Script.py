import urllib2
import json

class API ():
	def __init__(self):		
 		self.API_KEY = '&key=AIzaSyBhsQNMJrgBOdvEnfL33hTr5O9ZPSI14wk'

 	def Coordenada_por_Endereco (self, endereco = []):
 		geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
 		endereco_formatado = 'address='
 		
 		for i in endereco:
 			if type(i) != int:
 				aux = i.split(' ')
 			else:
 				aux = str(i)
 			for j in aux:  
 				endereco_formatado += j + '+'

 		requisicao = geocode_url + endereco_formatado + self.API_KEY
 		resposta = urllib2.urlopen(requisicao).read()
 		resposta = json.loads(resposta)
 		dado = [resposta['results'][0]['geometry']['location']['lat'], resposta['results'][0]['geometry']['location']['lng']]
 		
 		return dado
 		
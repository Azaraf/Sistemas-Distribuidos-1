#ESTE ES EL STUB

import socket
import json

class Tarea():
	def __init__(self):
		self.s = socket.socket()
		self.router = {'suma': { 'ip': '127.0.0.1', 'puerto': 5002 }, 'resta': { 'ip': 5001, 'puerto': 5000 }, 'multiplicacion': { 'ip': 5001, 'puerto': 5000 }, 'division': { 'ip': 5001, 'puerto': 5000 }}

	def suma(self, x, y):
		self.s.connect((self.router['suma']['ip'], self.router['suma']['puerto']))
		while True:
			mensajeS = json.dumps({'funcion': 'suma', 'x': x, 'y': y})
			self.s.send(mensajeS)
			respuesta = self.s.recv(4096)
			if respuesta:
				return respuesta

	def resta(x, y):
		# aqui se debe conectar con otro servidor y ver si tiene el metodo resta
		return resp

	def cerrar(self):
		self.s.close()




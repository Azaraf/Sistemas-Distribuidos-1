#Suma.py
import socket
import json


def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("", 5002))
	s.listen(1)
	while True:
		sc, addr = s.accept()
		recibido = sc.recv(4096)
		if recibido:
		    msj = json.loads(recibido)

		    if recibido == "close":
		        break

		    if msj['funcion'] == "suma":
		    	respuesta = int(msj['x']) + int(msj['y'])
		 
		    #Si se reciben datos nos muestra la IP y el mensaje recibido
		    print str(addr[0]) + " pidio: ", msj['funcion']
		 
		    #Devolvemos el mensaje al cliente
		    sc.send(str(respuesta))
		    sc.close()
	print "Adios."
	s.close()

if __name__ == "__main__":
	main()
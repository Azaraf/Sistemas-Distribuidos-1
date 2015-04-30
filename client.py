#!/usr/bin/env python
 
#importamos el modulo para trabajar con sockets
import socket
import json
 
#Creamos un objeto socket para el servidor. Podemos dejarlo sin parametros pero si 
#quieren pueden pasarlos de la manera server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
import sys
if sys.version_info < (3, 0):
	input = raw_input
 
#Nos conectamos al servidor con el metodo connect. Tiene dos parametros
#El primero es la IP del servidor y el segundo el puerto de conexion
s.connect(("127.0.0.1", 5000))
 
#Creamos un bucle para retener la conexion
while True:
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    funcion = raw_input("escriba la operacion (suma, resta, multiplicacion o division) >> ")
    x = raw_input("introduzca el primer valor >> ")
    y = raw_input("introduzca el segundo valor >> ")
    mensaje = json.dumps({'funcion': funcion, 'x': x, 'y': y})
 
    #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
    s.send(mensaje)

    recibido = s.recv(4096)
    print(recibido)
    
 
    #Si por alguna razon el mensaje es close cerramos la conexion
    if mensaje == "close":
        break
 
#Imprimimos la palabra Adios para cuando se cierre la conexion
print "Adios."
 
#Cerramos la instancia del objeto servidor
s.close()
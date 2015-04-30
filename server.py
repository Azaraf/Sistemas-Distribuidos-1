#!/usr/bin/env python
 
#importamos el modulo socket
import socket
from Tarea import Tarea
import json
 
#instanciamos un objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
#Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
#Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
s.bind(("", 5000))
 
#Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
#El numero de conexiones entrantes que vamos a aceptar

s.listen(1)
 
#Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este 
#devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
#tarea = Tarea()
sc = None
 
while True:
 
    #Recibimos el mensaje, con el metodo recv recibimos datos y como parametro 
    #la cantidad de bytes para recibir
    if not sc:
        sc, addr = s.accept()
    else:
        tarea = Tarea()
        recibido = sc.recv(4096)
        msj = json.loads(recibido)
        #Si el mensaje recibido es la palabra close se cierra la aplicacion
        if recibido == "close":
            break
     
        print str(addr[0]) + " quiere hacer una: ", msj["funcion"]

        funciones = {'suma': tarea.suma, 'resta': tarea.resta}
        resultado = funciones[msj["funcion"]](msj["x"], msj["y"])
        print str(" La respuesta es: "), resultado
     
        #Devolvemos el mensaje al cliente
        sc.send(resultado)
        tarea.cerrar()
        if not sc:
            sc.close()
            sc = None
print "Adios."
 
#Cerramos la instancia del socket cliente y servidor
s.close()
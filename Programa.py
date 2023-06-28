
import ping3
import time
import datetime
import configparser

from configparser import ConfigParser

config = configparser.ConfigParser()
config.read('config.ini')

Ttotal = config['PING', 'tiempo']
hostname = config['PING', 'ip']
tiempo = config['PING', 'cadencia']
pings = (Ttotal * 60) / tiempo

'''
hostname = input("A que ip quieres hacer ping?   ")
pings = int(input("Cuantos pings quieres hacer?    "))
tiempo = int(input("con cuantos segundos de diferencia?    "))
'''
print ("Tiempo total:", Ttotal, "minutos / IP: ", hostname, "/ Separacion (seg)", pings)
nombre = "registro ping a " + hostname + ".txt"
print ("guardando en arxivo:", nombre)

with open(nombre, 'w') as archivo:
        archivo.write("Inicio del recuento de pings")

while pings != 0:
        pings -= 1
        respuesta = ping3.ping(hostname)
        hora = datetime.datetime.now()
        if respuesta is not None:
                with open(nombre, 'a') as archivo:
                        resp = "\nFUNCIONA       " + str(hora)
                        archivo.write(resp)
                print ("Ping con exito    ", hora)
        else:
                with open(nombre, 'a') as archivo:
                        resp = "\nFALLA           " + str(hora)
                        archivo.write(resp)
                print ("ping sin exito   ", hora)
        time.sleep(tiempo)



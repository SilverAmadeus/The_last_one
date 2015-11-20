import os
import os.path #por si las dudas ahorita que fluya mas veo si es necesaria o no
import subprocess 
import sys


def manejoZIP():
	subprocess.call(['tree','-X','-Q','-o','master.txt'])

#This is it...
#FOR FILES
def ar_c(name):
	try:
		file = open(name,'a') # file no es una palabra reservada amigo?
		file.close()
		print("Archivo creado")
	except:
		print('Something went wrong! Cant tell what?')

def ar_r(name):
	try:
		if os.path.isfile(name):
			arch = open(name, "r") #DEFINIMOS QUE LO PASE CON TODO Y EXTENSION
			for line in archivo.readlines():
				print line
			arch.close()
		else:
			print "El fichero no existe"
	except:
		print('Something went wrong! Cant tell what?')

def ar_pos(name): #Posicion actual del puntero
	try:
		if os.path.isfile(name):
			arch = open(name, "r") 
			print arch.tell()
		else:
			print "El fichero no existe"
	except:
		print('Something went wrong! Cant tell what?')




#FOR DIRECTORIES
def deleteFile(name):
	os.remove(name) #name is a string

def dir_map():
	subprocess.call(['tree'])	
	origin/master

r = 0
print("\n\n\t\t.:: Sistema de Archivos ::.\n")
while (r != 'q'):

	print("\t-- Comandos: To be added, h: Para ayuda --")
	r = raw_input(": ")
	if(r == 'h'):
		print("\t\tdir_map: Muestra contenido del directorio\n"
			+ "\t\tar_c: Crea un archivo\n"
			+ "\t\tq: Salir del sistema\n")
		raw_input("Press Enter to continue...")
	if(r == 'ar_c'):
		# Llamada a funcion con raw_input como valor que se espera en el teclado, espero no te nortee. :P
		ar_c(raw_input("Nombre del archivo: ")+'.txt') 

	if r == 'dir_map':
		dir_map()
	elif(r != 'q'):
		print("Comando invalido\n")
print("Exiting...")


import os
import subprocess 
import sys

#This is it...
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
	elif(r != 'q'):
		print("Comando invalido")
print("Exiting...")

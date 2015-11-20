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
        f = open(name,'a')
        f.close()
        print("Archivo creado")
        return True
    except:
        print('Something went wrong! Cant tell what?')

def ar_r(name):
    try:
        if os.path.isfile(name):
            arch = open(name, "r") #DEFINIMOS QUE LO PASE CON TODO Y EXTENSION
            for line in arch.readlines():
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

def ar_w(name):
    try:
        if os.path.isfile(name):
            arch = open(name, "r")
            print "\t\tEscribe 'quit para salir del editor\n\t\tESTE METODO SOBRE ESCRIBE EL ARCHIVO\n" \
                  "\t\tContenido del archivo:\n"
            for line in arch.readlines():
                print line
            arch.close()
            arch = open(name, "w+")
            lines = []
            lp = 0
            while(lp != 'quit\n'):
                lp = raw_input(": ")+"\n"
                if lp != 'quit\n':
                    lines.append(lp)
            arch.writelines(lines)
            arch.close()

        else:
            print "El fichero no existe"
    except:
        print('Something went wrong! Cant tell what?')

#FORDIRECTORIES
def deleteFile(name):
    os.remove(name) #name is a string

def dir_map():
    subprocess.call(['tree'])

r = 0
print("\n\n\t\t.:: Sistema de Archivos ::.\n")
while (r != 'q'):

    print("\t-- Comandos: To be added, h: Para ayuda --")
    r = raw_input(": ")
    if(r == 'h'):
        print("\t\tdir_map: Muestra contenido del directorio\n"
              + "\t\tar_c: Crea un archivo\n"
              + "\t\tar_r: Muestra contenido de un archivo\n"
              + "\t\tar_w: Escribe en un archivo (Sobre escribe contenido\n"
              + "\t\tq: Salir del sistema\n")
        raw_input("Press Enter to continue...")
    elif(r == 'ar_c'):
        # Llamada a funcion con raw_input como valor que se espera en el teclado, espero no te nortee. :P
        ar_c(raw_input("Nombre del archivo: ")+'.txt')
        raw_input("Press Enter to continue...")
    elif(r == 'ar_r'):
        ar_r(raw_input("Nombre del archivo: ")+'.txt')
        raw_input("Press Enter to continue...")
    elif(r == 'dir_map'):
        dir_map()
        raw_input("Press Enter to continue...")
    elif(r == 'ar_w'):
        ar_w(raw_input("Nombre del archivo: ")+'.txt')
    else:
        print("Comando invalido\n")
print("Exiting...")


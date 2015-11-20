import os
import os.path #por si las dudas ahorita que fluya mas veo si es necesaria o no
import subprocess
import shutil
import datetime
import sys

date = datetime.datetime.now()

def manejoZIP():
    subprocess.call(['tree','-X','-Q','-o','master.txt'])

def entryFolder(name):
    try:
        os.chdir(name)
    except:
        print "This folder doesn't exist"

def returnFoder():
    

def dir_c(name):
    os.mkdir(name)

def move(src, dst):
    try:
        shutil.move(src, dst)
    except:
        print "Parametros erroneos"
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
            print("\t-- Contenido del archivo " + name+ " --\n")
            for line in arch.readlines():
                print line
            print("\n\t----------------------------------\n")
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

def ar_sk(name, pos): #pos is in bytes
    try:
        if os.path.isfile(name):
            int(pos)
            print "Use: \n0)Start to final\n1)Now to final\n2)Final to Start\n"
            mode = int(raw_input(": "))
            arch = open(name, "r+")
            if mode == 0: #posicionar desde el inicio USE (TO,START)
                arch.seek(pos, mode) #De inicio hacia delante
            elif mode == 1:
                arch.seek(pos, mode) #De la posicion actual hacia delante
            elif mode == 2:
                arch.seek(-pos, mode) #Del final hacia atras
            else:
                print("You didn't choose any right option")
        else:
            print "El fichero no exite"
    except:
        print "Something went wrong! Can't tell what?"


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
              + "\t\tar_r: Muestra el contenido de un archivo\n"
              + "\t\tdir_c: Crea una carpeta en el directorio que se esta trabajando, si se toma archivo se debe especificar\n"
              + "\t\tmove: Mueve un archivo o carpeta a un directorio destino, si el primer parametro es un archivo se debe agregar extension\n"
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
        raw_input("Press Enter to continue...")
    elif(r == 'dir_c'):
        dir_c(raw_input("Nombre de la carpeta: "))
        raw_input("Press Enter to continue...")
    elif(r == 'ar_sk'):
        ar_sk(raw_input("Nombre del archivo: ")+'.txt', int(raw_input("Desplazamiento: ")))# Se puede hacer esto? pasar dos argumentos uno leido despues de otro?
        raw_input("Press Enter to continue...")
    elif(r == 'move'):
        move(raw_input("Fuente(Si es archivo especifica extension): "), raw_input("Destino: "))
        raw_input("Press Enter to continue...")
    else:
        if r == 'q':
            pass
        else:
            print("Comando invalido\n")
subprocess.call(['tree','-X','-o', str(date.strftime('%Y|%m l%d %H;%M;%S')) +'_master.txt'])
print("Exiting...")


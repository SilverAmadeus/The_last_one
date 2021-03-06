import os
import subprocess
import shutil
import datetime
import sys


mount = os.getcwd() #carpeta de montaje

#FORDIRECTORIES

def manejoZIP():
    subprocess.call(['tree','-X','-Q','-o','master.txt'])

def entryFolder(name):
    try:
        os.chdir(name)
    except:
        print "This folder doesn't exist"

def returnFolder():
    if mount != os.getcwd():
        os.chdir('..')
    else:
        print "No puedes salir del sistema de archivos"

def deleteFolder(name):
    try: 
        shutil.rmtree(name)
    except:
        print "This folder doesn't exist"   

def dir_c(name):
    try:
        alterna = os.listdir('.')
        if alterna.count(name)>0:
            print "No puedes crear una carpeta dos veces."
        else:
            os.mkdir(name)
            print "Carpeta creada exitosamente."
    except:
        print "Something went wrong! Can't tell what?"

def move(src, dst):
    try:
        shutil.move(src, dst)
    except:
        print "Parametros erroneos"


def dir_map():
    subprocess.call(['tree'])

#FOR FILES

def ar_c(name):
    try:
        lista = os.listdir('.') #lista de archivos en la carpeta actual
        if lista.count(name)>0:
            print "No puedes crear el mismo archivo sobre la misma carpeta"
        else:    
            f = open(name,'a')
            f.close()
            print("Archivo creado")
    except:
        print('Something went wrong! Cant tell what?')

def deleteFile(name):
    try:
        alt = os.listdir('.')
        if alt.count(name)>0:
            os.remove(name) #name is a string
        else:
            print "No puedes eliminar un archivo que no existe D:"
    except:
        print "Something went wrong! Can't tell what?"

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
                cnt = arch.read(pos)
                print cnt
            elif mode == 1:
                arch.seek(pos, mode) #De la posicion actual hacia delante
                cnt = arch.read(pos)
                print cnt
            elif mode == 2:
                arch.seek(-pos, mode) #Del final hacia atras
                cnt = arch.read(pos)
                print cnt
            else:
                print("You didn't choose any right option")
        else:
            print "El fichero no exite"
    except:
        print "Something went wrong! Can't tell what?"


r = 0
print("\n\n\t\t\t\t.:: Sistema de Archivos ::.\n")
while (r != 'q'):

    print("\n\t-- Comandos: dir_map   ar_c   ar_r   ar_w   ar_sk   dir_c   dir_en   ar_dl   dir_ret  dir_dl   move   --"
          "\n\n\t--\t\t\t q: Salir     h: Descripcion de los comandos                                      --")
    r = raw_input(": ")
    if(r == 'h'):
        print(  "\t\tdir_map:   Muestra contenido del directorio\n"
              + "\t\tar_c:      Crea un archivo\n"
              + "\t\tar_r:      Muestra contenido de un archivo\n"
              + "\t\tar_w:      Escribe en un archivo (Sobre escribe contenido)\n"
              + "\t\tar_sk:     Reposiciona el puntero a una posicion dada en bytes mostrando los caracteres del desplazamiento\n"
              + "\t\tdir_c:     Crea una carpeta en el directorio que se esta trabajando, si se toma archivo se debe especificar\n"
              + "\t\tdir_en:    Entre a la carpeta que se encuentra en el directorio actual\n"
              + "\t\tar_dl:     Borra un archivo existente \n"
              + "\t\tdir_ret:   Permite regresar por los directorios hasta llegar al base\n"
              + "\t\tdir_dl:    Borra una carpeta especifica junto con los contenidos\n"
              + "\t\tmove:      Mueve un archivo o carpeta a un directorio destino, si el primer parametro es un archivo se debe agregar extension\n"
              + "\t\tq:         Salir del sistema\n")
        raw_input("Press Enter to continue...")
    elif(r == 'ar_c'):
        # Llamada a funcion con raw_input como valor que se espera en el teclado, espero no te nortee. :P
        ar_c(raw_input("Nombre del archivo: ")+'.txt')
        raw_input("Press Enter to continue...")
    elif(r == 'ar_r'):
        ar_r(raw_input("Nombre del archivo: ")+'.txt') #checar si esto funciona si la extencion txt
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
    elif(r == 'dir_en'):
        entryFolder(raw_input("Nombre de la carpeta: "))
        raw_input("Press Enter to continue...")
    elif(r == 'dir_dl'):
        deleteFolder(raw_input("Nombre de la carpeta: "))
        raw_input("Press Enter to continue...")
    elif(r == 'ar_sk'):
        ar_sk(raw_input("Nombre del archivo: ")+'.txt', int(raw_input("Desplazamiento: ")))# Se puede hacer esto? pasar dos argumentos uno leido despues de otro?
        raw_input("Press Enter to continue...")
    elif(r == 'ar_dl'):
        deleteFile(raw_input("Nombre del archivo: ")+'.txt')
        raw_input("Press Enter to continue...")
    elif(r == 'move'):
        move(raw_input("Fuente(Si es archivo especifica extension): "), raw_input("Destino: "))
        raw_input("Press Enter to continue...")
    elif(r == 'dir_ret'):
        returnFolder()
        raw_input("Press Enter to continue...")
    else:
        if r == 'q':
            pass
        else:
            print("Comando invalido\n")
date = datetime.datetime.now()


while not os.getcwd()==mount:
    os.chdir('..')

subprocess.call(['tree','-X','-o', str(date.strftime('%Y|%m l%d %H;%M;%S')) +'_master.txt'])
print("Exiting...")
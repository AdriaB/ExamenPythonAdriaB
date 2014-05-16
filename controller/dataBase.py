__author__ = 'adria'

import sys
sys.path.insert(0, '../model')
from aplicacion import *
import os.path
import datetime

class DataBase:
    def __init__(self, rutafitxer="../database/aplicacions.txt"):
        """Iniciamos la classe con al ruta de la base de datos"""
        self.rutafitxer = rutafitxer

    def afegeixAplicacio(self, aplicacion):
        """Añade una aplicación al fichero de aplicaciones"""
        added = False
        exists = False
        if os.path.isfile(self.rutafitxer):
            #comprovar que l'aplicacio no existeixi
            with open(self.rutafitxer, 'r') as f:
                resultat = f.read()
            for l in resultat.split("\n"):
                if(l.split(";")[0] == aplicacion.nombre):
                    exists = True
            if not exists:
                with open(self.rutafitxer, 'a') as f:
                    f.write(aplicacion.nombre+";"+aplicacion.proveedor+";"+aplicacion.fecha+";"+str(aplicacion.precio)+";"+str(aplicacion.descargas)+";"+str(aplicacion.puntuaciones)+";"+str(aplicacion.puntuacion)+";"+str(aplicacion.comentarios)+";\n")
                    added = True
        else:
            print("Error! No se ha podido encontrar el fichero de aplicaciones!")

        return added

    def sumarDescarga(self, nombre):
        """Suma una descarga a la aplicación con ese nombre. Devuelve True o False en funcion de si se ha encontrado (y modificado) o no"""
        if os.path.isfile(self.rutafitxer):
            file = open(self.rutafitxer, 'r')
            llista = file.readlines()
            file.close()
            trobat = False
            with open(self.rutafitxer, 'w') as file:
                for linia in llista:
                    if linia.split(";")[0] != nombre:
                        file.write(linia)
                    else:
                        linia1 = linia.split(";")
                        descargues = int(linia.split(";")[4])
                        resultat = linia1[0]+";"+linia1[1]+";"+linia1[2]+";"+linia1[3]+";"+str(descargues+1)+";"+linia1[5]+";"+linia1[6]+";"+linia1[7]
                        file.write(resultat)
                        trobat = True
        else:
            print("Error! No se ha podido encontrar el fichero de aplicaciones!")
        return trobat

    def sumarComentario(self, nombre):
        """Suma un comentario a la aplicación con ese nombre. Devuelve True o False en funcion de si se ha encontrado (y modificado) o no"""
        if os.path.isfile(self.rutafitxer):
            file = open(self.rutafitxer, 'r')
            llista = file.readlines()
            file.close()
            trobat = False
            with open(self.rutafitxer, 'w') as file:
                for linia in llista:
                    if linia.split(";")[0] != nombre:
                        file.write(linia)
                    else:
                        linia1 = linia.split(";")
                        comentarios = linia.split(";")[7]
                        comentarios = int(comentarios)
                        resultat = linia1[0]+";"+linia1[1]+";"+linia1[2]+";"+linia1[3]+";"+linia1[4]+";"+linia1[5]+";"+linia1[6]+";"+str(comentarios+1)+"\n"
                        file.write(resultat)
                        trobat = True
        else:
            print("Error! No se ha podido encontrar el fichero de aplicaciones!")
        return trobat
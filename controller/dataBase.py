__author__ = 'adria'

import sys
sys.path.insert(0, '../model')
from aplicacion import *
import os.path
import datetime

class DataBase:
    def __init__(self, rutafitxer="../database/aplicacions.txt"):
        """Iniciem la classe amb al ruta de la base de dades"""
        self.rutafitxer = rutafitxer

    def afegeixAplicacio(self, aplicacion):
        """Afegeix una aplicacio al fitxer d'aplicacions"""
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
            print("Error! couldn't find apps' file")

        return added
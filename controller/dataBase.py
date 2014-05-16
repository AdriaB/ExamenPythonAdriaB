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

    def listApps(self, type):
        __author__ = "Aram Miquel"
        print("Listing Apps ordered by our ranking...")
        freeAppList = list()
        with open(self.rutafitxer, "r") as f:
            for line in f:
                freeAppList.append(line)
        appUnorderedList = freeAppList
        appOrderedList = list()
        for appString in appUnorderedList:
            name, developer, date, price, numberDownloads, numberScores, score, numberComments = appString.split(";")
            app = Aplicacion(name, developer, date, int(price), numberDownloads, numberScores, score, numberComments)
            if type == 0:
                if app.getPrice() == 0:
                    appScore = ((float(app.getNumberDownloads()) * 0.6) + (float(app.getScore()) * 0.25) + (float(app.getNumberComments()) * 0.15))
                    appToList = (app, appScore)
                    appOrderedList.append(appToList)
            elif type == 1:
                if app.getPrice() > 0:
                    appScore = ((float(app.getNumberDownloads()) * 0.6) + (float(app.getScore()) * 0.25) + (float(app.getNumberComments()) * 0.15))
                    appToList = (app, appScore)
                    appOrderedList.append(appToList)
            else:
                print("Internal error. You should not be here.")
        self.printOrderedList(appOrderedList)


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
                    f.write(aplicacion.nombre+";"+aplicacion.proveedor+";"+aplicacion.fecha+";"+str(aplicacion.precio)+";"+str(aplicacion.descargas)+";"+str(aplicacion.puntuaciones)+";"+str(aplicacion.puntuacion)+";"+str(aplicacion.comentarios)+"\n")
                    added = True
        else:
            print("Error! No se ha podido encontrar el fichero de aplicaciones!")

        return added

    def printOrderedList(self, orderedList):
        __author__ = "Aram Miquel"
        maxScore = 0;
        for app in orderedList:
            if app[1] > maxScore:
                maxScore = app[1]
        for app in orderedList:
            if app[1] == maxScore:
                print(app[0].getName() + " with score " + str(app[1]))
                orderedList.remove(app)
        if orderedList:
            self.printOrderedList(orderedList)

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
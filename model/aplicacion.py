__author__ = 'adria'

class Aplicacion:
    def __init__(self, nombre, proveedor, fecha, precio, descargas, puntuaciones, puntuacion, comentarios):
        self.nombre = nombre
        self.proveedor = proveedor
        self.fecha = fecha
        self.precio = precio
        self.descargas = descargas
        self.puntuaciones = puntuaciones
        self.puntuacion = puntuacion
        self.comentarios = comentarios

    def getName(self):
        return self.nombre
    def getDeveloper(self):
        return self.proveedor
    def getDate(self):
        return self.fecha
    def getPrice(self):
        return self.precio
    def getNumberDownloads(self):
        return self.descargas
    def getNumberScores(self):
        return self.puntuaciones
    def getScore(self):
        return self.puntuacion
    def getNumberComments(self):
        return self.comentarios

    def insertToDb(self):
        appLine = self.nombre + ";" + self.proveedor + ";" + self.fecha + ";" + str(self.precio) + ";" + str(self.descargas) + ";" + str(self.puntuaciones) + ";" + str(self.puntuacion) + ";" + str(self.comentarios)
        #database = DbController()
        #database.insertLine(appLine)

    def calcTotalMoneyEarned(self):

        totalMoney = float(self.price) * float(self.numberDownloads)
        if self.price == 0:
            print("Free apps don't have this option!")
        else:
            print("Total money earned with selled: " + str(totalMoney))

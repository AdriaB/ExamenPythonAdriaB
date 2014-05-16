__author__ = 'adria'

from dataBase import *

while True:
    print("___ Menú: ___")
    print("1. Mostrar lista de aplicaciones (gratuitas o de pago)")
    print("2. Añadir nueva aplicacion")
    print("3. Modificar datos identificacion de una aplicación")
    print("4. Sumar una descarga")
    print("5. Sumar un comentario")
    print("6. Salir")
    opcion = input("Introduce una opcion: ")
    d = DataBase()
    if opcion == "1":
        pass
    elif opcion == "2":
        print("Escribe los datos de la aplicación:")
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        nombre = input("Escribe el nombre de la aplicación a modificar: ")
        modify = d.sumarDescarga(nombre)
        if modify:
            print("Se ha añadido una descarga correctamente")
        else:
            print("No se ha podido añadir una descarga. Compruebe que ha escrito el nombre correctamente")
    elif opcion == "5":
        nombre = input("Escribe el nombre de la aplicación a modificar: ")
        modify = d.sumarComentario(nombre)
        if modify:
            print("Se ha añadido un comentario correctamente")
        else:
            print("No se ha podido añadir un comentario. Compruebe que ha escrito el nombre correctamente")
    elif opcion == "6":
        print("Has salido correctamente")
        break
    else:
        print("Opcion incorrecta")
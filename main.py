import json
import os,time

#ruta archivo
archivoJson= "biblioteca.json"

def abrirLista(rutaJson):
    with open(rutaJson, "r") as salida:
        archivo=json.load(salida)
    return archivo

short_abrirLista= abrirLista(archivoJson)

def listar(archivo):
    print("Listado de autores: ")
    for listar in short_abrirLista["Autor"]:
        print(listar)

def guardarDatos(datos,rutaJson):
    with open(rutaJson, "w") as salida:
        json.dump(datos,salida,indent=4)
    
#datos,rutajson
def agregarAutor(rutaJson):
    print("Agregar autor")

    #idAgregar=int(input("Agregar ID: "))
    autorAgregar=input("Nombre autor: ")
    nacionalidadAgregar=input("Nacionalidad autor: ")
 
    dict_agregarAutor={
        "AutorID": 21, #
        "Nombre": autorAgregar,
        "Nacionalidad": nacionalidadAgregar
    }
    rutaJson["Autor"].append(dict_agregarAutor)
    guardarDatos(rutaJson,archivoJson)

def metodo_actualizarAutor(archivo):
    print("")
    buscador=input("Ingresa nombre autor a editar: ")
    for iterador in archivo["Autor"]:
        if iterador["Nombre"]==buscador:
            #print(iterador)
            for clave, valor in iterador.items():
                print(f"{clave}: {valor}")
            return iterador
def actualizarAutor(archivo):
    persona= metodo_actualizarAutor(short_abrirLista)
    
    nombreNuevo=input("Ingresa nombre nuevo: ")
    nacionalidadNuevo=input("Ingresa nacionalidad nueva: ")
    persona["Nombre"]= nombreNuevo
    persona["Nacionalidad"]= nacionalidadNuevo
    
    guardarDatos(archivo,archivoJson)



def eliminarAutor(archivo):
    quitarAutor= input("Ingrese nombre del autor a eliminar: ")
    for iterador in archivo["Autor"]:
        if iterador["Nombre"]==quitarAutor:
            #print(iterador)
            for clave, valor in iterador.items():
                print(f"{clave}: {valor}")
            archivo["Autor"].remove(iterador)
            guardarDatos(archivo,archivoJson)

def menuAutor():
    while True:
        print("---------------------")
        print("  MANTENEDOR AUTORES ")
        print("---------------------")
        print("")
        print("[1] Agregar Autor ")
        print("[2] Editar Autor ")
        print("[3] Eliminar Autor ")
        print("[4] Buscar Autor ")
        print("[5] Volver ")

        opcion=int(input("Ingrese una opcion: "))
        if opcion==1:
            
            agregarAutor(short_abrirLista)
        if opcion==2:
            actualizarAutor(short_abrirLista)
        if opcion==3:
            eliminarAutor(short_abrirLista)
        if opcion==4:
            listar(short_abrirLista)
        if opcion==5:
            break
        return
    


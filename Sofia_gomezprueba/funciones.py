import csv

juegos_csv = 'productos.csv'

def Filtrar_cada_palabra(juegos):
    juego=input("Ingrese la una palabra: ")
    for juego in juegos_csv:
        print(juego)
     
    with open ('Juegos.csv','w',newline='') as archivo:
        escritor=csv.writer(archivo,delimiter=',')


    print("Archivo creado exitosamente")


def Promedio_por_consola():
    nombre_consola=input("ingrese el nombre de la conosola: ")
    #Diccionario:
    print("El precio promedio de los juegos es: ")

def Cantidad_por_año():
    año=int(input("Ingrese eñ año a consultar: "))
    print("Archivo creado exitosamente")
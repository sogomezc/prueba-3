import funciones as fn 

    
    
juegos= {}


while True:
    print("**Bienvenido/a**")
    print("1.- Filtrar cada palabra")
    print("2.- Promedio por consola ")
    print("3.- Cantidad por año")
    print("4.- Salir del programa")

    opcion=int(input("Ingresar una opcion: "))

    if opcion==1:
        fn.Filtrar_cada_palabra()
    elif opcion==2:
        fn.Promedio_por_consola()
    elif opcion==3:
        fn.Cantidad_por_año()
    elif opcion==4:
        print("Saliendo del programa...")
        break
    else:
        print("Ingrese una opcion valida del 1 al 4")

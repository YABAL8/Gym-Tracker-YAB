# Diario de ejercicios de mi dia a dia usando txt
import os
from dia_12_funciones import historial_ejercicios, buscar_ejercicio, ingresar_ejercicio
#modo menu principal
while True:
    os.system('cls')
    print("\n--- GYM TRACKER YAB ---")
    print("1. Ingresar Nuevo Ejercicio")
    print("2. Ver Historial de Ejercicios")
    print("3. Buscar Ejercicio Especifico")
    print("4. Salir")

    opcion = input("\nElija una opcion (1-4): ")

    #agregar ejercicio
    
    if opcion == "1":
        ingresar_ejercicio()  


    #ver historial
    elif opcion == "2":
        historial_ejercicios()

    #buscador
    elif opcion == "3":
        buscar_ejercicio()          
            
    #salir
    elif opcion == "4":
        exit()
                  
    else:
        print("Error, solo datos validos (1-4)")
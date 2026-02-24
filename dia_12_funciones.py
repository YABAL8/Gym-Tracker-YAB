#introduccion a los modulos o funciones

#funcion
def saludo_personalizado():
    
    ejercicio = input("Hola mi rey, nuevo dia, que te toca entrenar hoy?: ")
    print(f"A darle con todo a {ejercicio} fiera!")
    
#programa principal
#print("........................")
#saludo_personalizado()
#print("........................")

#Funciones para el tracker gym yab

#opcion1
def ingresar_ejercicio ():
    """Ingresa valores para guardarlos en la memoria
    """
    
    print("\nIngrese sus datos para registrar su progreso diario")
    while True:
            # El usuario ingresa sus datos
            ejercicio = input("¿Que ejercicio ha realizado o quiere ingresar?:  ")
            
            # validacion de error try except
            while True:
                try:
                    peso = float(input(f"¿Cuanto peso ha levantado en {ejercicio}?(Kg):  "))
                    break # Si el numero es flotante se termina el while, si no except value error
                except ValueError:
                    print("Error: ¡Solo ingresa numeros!")

            # la vaina del txt para guardarlo permanentemente
            with open("Historial_de_pesos.txt", "a") as archivo:
                archivo.write(f"Ejercicio: {ejercicio} | Peso: {peso} kg\n")
                
            continuar = input("\nDesea ingresar otro ejercicio?(Si/No): ").lower()
            if continuar == "si":
                print("\nContinuando...")
            
            elif continuar == "no":
                break
            
            else:
                print ("Error, dato invalido, ingrese de nuevo: (Si/No)\n") 

#opcion2
def historial_ejercicios ():
    """Muestra todo el registro de los ejercicios añadidos
    """
    with open("Historial_de_pesos.txt", "r") as archivo:
                historial = archivo.read()
                
                print (f"Historial de pesos: \n{historial}")
                
                input("\nPresiona ENTER para volver al menu")
                
# opcion 3
def buscar_ejercicio():
    """Busqueda de un ejercicio en especifico
    """
    while True:
            print("\nModo buscador: ")
            busqueda = input("¿Que ejercicio Buscas?: ").lower()
            
            with open("Historial_de_pesos.txt", "r") as archivo:
                lista_de_lineas = archivo.readlines()  # Convierte el texto en una lista
                
                contador = 0
                found = False
                for linea in lista_de_lineas:
                    #si la palabra que busco esta dentro de esta lista...
                    if busqueda in linea.lower():
                        print(linea.strip())  #strip() quita los espacio extra
                        found = True
                        contador += 1
                
                if found:
                    print(f"Se encontro {contador} resultados...")
                        
                else:
                    print(f"No se encontro registros de {busqueda}.")  
                
            continuar = input("\nDesea buscar otro ejercicio?(Si/No): ").lower()
            if continuar == "si":
                print("Continuando...\n")
            
            elif continuar == "no":
                break
            
            else:
                print ("Error, dato invalido, ingrese de nuevo: (Si/No)\n") 
                

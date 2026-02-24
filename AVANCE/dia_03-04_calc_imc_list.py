print("-------CALCULADORA DE INDICE DE MASA CORPORAL-------")
print(" ")

print("El Indice de Masa Corporal (IMC) es un indicador simple y estandarizado que- \nrelaciona el peso y la estatura de una persona para clasificar si tiene un peso saludable, bajo peso, sobrepeso u obesidad.")

print(" ")

#listas
pacientes = []
resultados_imc = []

# bucle
while True:
    #el usuario ingresa su nombre para una mayor UX jsajs
    nombre = input("Ingrese su nombre por favor:  ")
    print(" ")
    print(f"Mucho gusto {nombre}, gracias por usar nuestra calculadora de IMC, rellene las- \nsiguientes casillas con sus datos reales y exactos para una mejor precision sobre su condicion.")
    print(" ")
    #el usuario ingresa sus datoss + uso del try except
    try:
        peso = float(input("Ingrese su peso actual en kilogramos (Kg):  "))

        altura = float(input("Ingrese su altura actual en metros (m):  "))
        
        #correccion por si pone 0 el usuario
        if altura <= 0:
            print("Error: NO creo que seas tan enano mi rey")
            continue
    
        imc = peso / (altura * altura)
    
        if imc >= 30:
            print(f"{nombre} tu IMC es de {imc:.2f}, esto indica Obesidad: Cuidado rey, pegale una dieta y haz ejercicio, es por tu salud!")
        elif imc >= 25:
            print (f"{nombre} tu IMC es de {imc:.2f}, esto indica Sobrepeso: A ajustar esos macros mi rey, un cadio hiit y listo!")
        elif imc >= 18.5:
            print (f"{nombre} tu IMC es de {imc:.2f}, esto indica que estas en tu Peso Indicado: Sigue asi mi rey!")
        else:
            print (f"{nombre} tu IMC es de {imc:.2f}, esto indica que estas Bajo de Peso: Tienes que comer mass, echale mas proteina y carbos diarios, es por salud mi rey!")
        
    except ValueError:
        #validacion del error
        print("Error!!!!!!!!, debes ingresar tus datos en numeros!")
    
    #guardado de datos
    print(f"Guardando datos de {nombre}...")
    pacientes.append(nombre)
    resultados_imc.append(round(imc,2))
    
    while True:
        continuar = input("\n Desea volver a calcular su IMC? (S/N):  ").lower()
        
        if continuar == 'n':
        
            print("\nREPORTE FINAL")
            print(f"Pacientes atendidos en total: {pacientes} ")
            print(f"Resultados: {resultados_imc}")
            print("Nos vemos rey")
            exit()
            
        elif continuar == 's':
            print ("REINICIANDO")
            print(" ")
            break
        
        else:
            print ("opcion incorrecta, por favor ingrese el valor solicitado: (S/N)")
            print(" ")
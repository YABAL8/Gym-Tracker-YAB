print("-------CALCULADORA DE INDICE DE MASA CORPORAL-------")
print(" ")

print("El Indice de Masa Corporal (IMC) es un indicador simple y estandarizado que- \nrelaciona el peso y la estatura de una persona para clasificar si tiene un peso saludable, bajo peso, sobrepeso u obesidad.")

print(" ")
#el usuario ingresa su nombre para una mayor UX jsajs
nombre = input("Ingrese su nombre por favor:  ")
print(" ")
print(f"Mucho gusto {nombre}, gracias por usar nuestra calculadora de IMC, rellene las- \nsiguientes casillas con sus datos reales y exactos para una mejor precision sobre su condicion.")
print(" ")
#el usuario ingresa sus datoss + uso del try except
try:
    peso = float(input("Ingrese su peso actual en kilogramos (Kg):  "))

    altura = float(input("Ingrese su altura actual en metros (m):  "))
    
    imc = peso / (altura * altura)
    
    if imc >= 30:
        print(f"{nombre} tu IMC es de {imc:.2f}, esto indica Obesidad: Cuidado rey, pegale una dieta y haz ejercicio, es por tu salud!")
    elif imc >= 25 and imc <= 29.9:
        print (f"{nombre} tu IMC es de {imc:.2f}, esto indica Sobrepeso: A ajudstar esos macros mi rey, un cadio hiit y listo!")
    elif imc >= 18.5 and imc <= 24.9:
        print (f"{nombre} tu IMC es de {imc:.2f}, esto indica que estas en tu Peso Indicado: Sigue asi mi rey!")
    else:
        print (f"{nombre} tu IMC es de {imc:.2f}, esto indica que estas Bajo de Peso: Tienes que comer mass, echale mas proteina y carbos diarios, es por salud mi rey!")
except ValueError:
    #validacion del error
    print("Error!!!!!!!!, debes ingresar tus datos en numeros!")
    
#Una mejor forma de representarlo pq si da la casualidad de que el IMC sale 29.95, no esta en mis parametros por ende saldra bajo de peso, para que o pase eso es mejor hacerlo asi pq
#toma absolutamente todos los numeros en el rango
# if imc >= 30:
  #  print(f"Obesidad... {imc:.2f}")
#elif imc >= 25: 
    # Python ya sabe que es MENOR a 30 por el 'if' anterior
    # Solo verificamos el piso (25)
#    print(f"Sobrepeso... {imc:.2f}")
#elif imc >= 18.5:
#    print(f"Peso Normal... {imc:.2f}")
#else:
#    print(f"Bajo peso... {imc:.2f}")
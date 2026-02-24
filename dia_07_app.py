from dia_07_motor_imc import calcular_imc, obtener_diagnostico

print ("--- CALCULADORA DE IMC MODULAR PRO ---")

while True:
    #inputs
    try:
        nombre = input ("\nNombre: ")
        peso = float(input ("peso en kg: "))
        altura = float(input("altura en m: "))
        
        if altura <= 0:
            print("altura invalida rey")
            continue
        
        #Aqui se usan las herramientas importadas
        #Phyton esta buscando 'calcular imc' en dia_07_ motor.py
        valor_imc = calcular_imc(peso, altura)
    
        #Phyton esta buscando 'obtener diagnostico' en dia_07_ motor.py
        texto_resultado = obtener_diagnostico(valor_imc)
    
        print(f"resultado para {nombre}: IMC {valor_imc}")
        print(f"diagnostico: {texto_resultado}")
    
    except ValueError:
        print("Error: Solo numeros por favo")
        
    salir = input("desea sali? (s/n): ")
    if salir == 's' : break
def calcular_imc(peso_kg, altura_m) :
    """recibe pso y altura, devuelve el IMC matematico"""
    imc_exacto = peso_kg / (altura_m * altura_m)
    return round(imc_exacto, 2)

def obtener_diagnostico (imc):
    """recibe el numero IMC y devuleve texto con el diagnostico"""
    if imc >= 30:
        return "Obesidad"
    elif imc >= 25:
        return "sobrepeso"
    elif imc >= 18.5:
        return "peso normal"
    else:
        return "bajo de peso"
    
print ("--- calculadora de imc modular ---")

while True:
    #inputs
    try:
        nombre = input ("\nNombre: ")
        peso = float(input ("peso en kg: "))
        altura = float(input("altura en m: "))
        
        if altura <= 0:
            print("altura invalida rey")
            continue
        
        #se llaman a las funciones
        valor_imc = calcular_imc(peso, altura)
    
        texto_resultado = obtener_diagnostico(valor_imc)
    
        print(f"resultado para {nombre}: IMC {valor_imc}")
        print(f"diagnostico: {texto_resultado}")
    
    except ValueError:
        print("Error: Solo numeros por favo")
        
    salir = input("desea sali? (s/n): ")
    if salir == 's' : break
    
    


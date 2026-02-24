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
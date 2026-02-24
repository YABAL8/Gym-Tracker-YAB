print("--CALCULANDO TUS HORAS DE ESTUDIO SEMANALES--")
#El usuario escribe su nombre
nombre = input("ESCRIBA SU NOMBRE:   ")

#Usamos el try/ exception para los errores, junto a condicionales
try:
    #El usuario ingresa sus horas de estudio
    horas_de_estudio = int(input(f"\n ¿Cuántas horas planeas estudiar al dia {nombre}? (Ingrese el valor en números):  " ))
    
    #El usuario escribe sus dias a la semana de estudio
    dias_de_estudio = int(input(f"\n ¿Cuántos dias planeas estudiar a la semana {nombre}? (Ingrese el valor en números): "))
    
    #calculo de las horas semanales
    horas_semanales = horas_de_estudio * dias_de_estudio
    print (f"Hola {nombre}!, estudiaras un total de {horas_semanales} horas semanales! ")
    
    #condicionales
    if horas_semanales > 15:
        print("Todo un maquina mi hermano, llegaras lejos!, cuidado con saturarte muchooooo")
    elif horas_semanales > 5:
        print("Sigue asi fiera, se que lograras tus objetivos!")
    else:
        print("Buen ritmo, pero debes estudiar bien profundo y sin distracciones mi rey!")
except ValueError:
    #validacion del error
    print(f"Error, datos invalido mi rey, intentalo de nuevo")
print("INICIANDO SESION")
print("Bienvenido Andres")

contraseña = "12345678"
numero_intentos = 5

while True:
    
    contraseña_ingresada = input("\nIngrese su contraseña por favor: ")
    if contraseña == contraseña_ingresada:
        print("Contraseña correcta, ingresando...")
        break
    else:
        print("Contraseña incorrecta, intentalo de nuevo por favor:")
        numero_intentos -= 1
        print(f"Intentos restantes: {numero_intentos}")
        if numero_intentos == 0:
            print("A alcanzado el limite de veces para ingresar su contraseña, bloqueando cuenta...")
            break
    
                    

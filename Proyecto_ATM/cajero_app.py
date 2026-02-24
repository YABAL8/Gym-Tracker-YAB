#cajero_app.py
from banco_logica import verificar_credenciales, obtener_saldo, retirar_dinero

print("--------------------------------------------")
print("         BIENVENIDO AL BANCO YABAL          ")
print("--------------------------------------------")

usuario_actual= None

#FASE 1: LOGIN
intentos = 3

while intentos > 0:
    usuario = input("\nIngrese su Usuario: ")
    pin = input ("Ingrese su PIN: ")
    
    # SE LLAMA AL CEREBRO, BANCO_LOGICA
    if verificar_credenciales (usuario, pin):
        print (f"Bienvenido, {usuario}!")
        usuario_actual = usuario # se guarda quien ingreso
        break
    else:
        intentos -= 1
        print (f"Incorrecto. Te quedan {intentos} intentos.")
        
    # si se acaban los intentos:
    if intentos == 0:
        print("TARGETA BLOQUEADA. CONTACTATE CON TU BANCO PARA PODER RECUPERARLA.")
        exit() #cierra el programa
        
# FASE 2: MENU PRINCIPAL
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar Saldo")
    print("2. Retirar Dinero")
    print("3. Salir")

    opcion = input("Elija una opción (1-3): ")

    if opcion == "1":
        # Usamos la otra función del cerebro
        dinero = obtener_saldo(usuario_actual)
        print(f"\nTu saldo es: ${dinero}")
    
    elif opcion == "2":
        print("\n--- RETIRO DE FONDOS ---")
        try:
            monto = float(input("¿Cuánto desea retirar?: "))
            
            # Validación básica (no puedes retirar negativos)
            if monto <= 0:
                print("Error: El monto debe ser mayor a 0.")
                continue

            # LLAMAMOS AL CEREBRO
            exito = retirar_dinero(usuario_actual, monto)

            if exito:
                # Si el cerebro dijo True
                print(f"Retiro exitoso. Tome sus ${monto}")
                # Opcional: Mostrar nuevo saldo
                nuevo_saldo = obtener_saldo(usuario_actual)
                print(f"Su nuevo saldo es: ${nuevo_saldo}")
            else:
                # Si el cerebro dijo False
                print("Fondos insuficientes.")
        
        except ValueError:
            print("Error: Ingrese un número válido.")
    
    elif opcion == "3":
        print("Gracias por usar Banco YABAL. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida.")
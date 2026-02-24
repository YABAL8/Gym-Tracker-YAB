#BANCO LOGICA

#BASE DE DATOS
#Cada usuario tiene su propio diccionario con 'pin' y 'saldo' 

usuarios = {
    "Andres" : {"pin": "1234" , "saldo" : 2000.00},
    "Admin" : {"pin" : "0000", "saldo" : 99999.99},
    "Pepe" : { "pin" : "1111" , "saldo" : 50.00}
}

#funciones de seguridad

def verificar_credenciales (usuario, pin_ingresado):
    """
    Devuelve True si el usuario existe y el pin coincide.
    Devuelve False si no.
    """
    if usuario in usuarios : 
        # Si el usuario existe, revisamos su PIN secreto
        if usuarios[usuario]["pin"] == pin_ingresado:
            return True
    return False

def obtener_saldo (usuario):
    """Devuelve el dinero que tiene el usuario."""
    
    return usuarios [usuario]["saldo"]

def retirar_dinero(usuario, monto_a_retirar):
    """
    1. Verifica si tiene saldo suficiente.
    2. Si tiene, resta el monto y devuelve True (Éxito).
    3. Si no tiene, devuelve False (Fondos insuficientes).
    """
    saldo_actual = usuarios[usuario]["saldo"]
    
    if monto_a_retirar > saldo_actual:
        return False # No le alcanza
    
    else:
        # Aquí modificamos la Base de Datos real
        usuarios[usuario]["saldo"] -= monto_a_retirar
        return True # Retiro exitoso
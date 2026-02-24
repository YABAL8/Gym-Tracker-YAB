# Tienda de calistenia (practica)
# Base de datos

inventario = {
    "pesas_5kg" : {"stock": 20, "categoria" : "pesas"},
    "magnesio" : {"stock" : 15, "categoria" : "accesorios"},
    "barra_polifuncional" : {"stock" : 10, "categoria" : "maquinas"},
    "guantes" : {"stock" : 30, "categoria" : "accesorios"},
    "straps" : {"stock" : 25, "categoria" : "accesorios"},
    "proteina" : {"stock" : 10, "categoria" : "suplementos"},
    "creatina" : {"stock" : 8, "categoria" : "suplementos"},
    "pesas_10kg" : {"stock" : 10, "categoria" : "pesas"},
    "pesas_15kg" : {"stock" : 10, "categoria" : "pesas"},
    "pesas_2.5kg" : {"stock" : 10, "categoria" : "pesas"},
    "pesas_7.5kg" : {"stock" : 10, "categoria" : "pesas"},
    "banca" : {"stock" : 6, "categoria" : "maquinas"},
    "maquinas_multifuncionales" : {"stock" : 3, "categoria" : "maquinas"},
    "omega_3" : {"stock" : 10, "categoria" : "suplementos"},
    
    
}

# MENU <>
print("--- Bienvenido a YAB-TRAIN ---")

while True:
    
    producto = input("¿Que deseas comprar?: ").lower()
    
    if producto in inventario:
        stock_actual = inventario[producto]["stock"]
        categoria_actual = inventario[producto]["categoria"]
        
        print(f"¡Si tenemos! Nos queda {stock_actual} unidades en la seccion {categoria_actual}.") 
        cantidad = int(input("\n¿Cuantas unidades desea llevar?: "))
        if cantidad <= 0:
            print("¡No puede llevar esa cantidad!")
        elif cantidad > stock_actual:
            print(f"¡No tenemos esa cantidad de unidades disponibles ahora! Contamos con {stock_actual} unidades por el momento.")
        else:
            inventario[producto]["stock"] -= cantidad
            print(f"¡Venta exitosa! Usted ha comprado un total de {cantidad} unidades de {producto}.")
        
        
    else:
        print(f"¡Lo sentimos mucho! No vendemos {producto} en YAB-TRAIN.")
        
    continuar = input("¿Desea comprar algo mas? (si/no): ").lower()
    if continuar == "no":
        print("¡Muchas gracias por comprar en YAB-TRAIN, vuelva pronto!")
        break
        




# movidas con el txt

print("--- SISTEMA DE GUARDADO ---")

# 1. MODO ESCRITURA ("w" - write)

with open("rutina.txt","w") as archivo:
    archivo.write("DIA 1 - PUSH (HOMBRO, PECHO Y TRICEPS)\n")
    archivo.write("DIA 2 - PULL (ESPALDA, BICEPS Y ANTEBRAZO)\n")
    archivo.write("DIA 3 - LEGS ( FULL PIERNA)\n")
    
print("Archivo creado y guardado exitosamente!\n")

# 3. MODO AGREGAR ("a" - append)
with open("rutina.txt","a") as archivo:
    archivo.write("DIA 4 - PUSH (HOMBRO, PECHO Y TRICEPS)\n")
    archivo.write("DIA 5 - PULL (ESPALDA, BICEPS Y ANTEBRAZO)\n")

# 2. MODO LECTURA ("r" - READ)

with open("rutina.txt","r") as archivo:
    contenido = archivo.read() #se guarda todo el texto en una variable
    print ("LEYENDO EL DISCO DURO...")
    print(contenido)
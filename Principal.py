import datetime
import os

# 1. Configurar el archivo de Excel
archivo = "inventario_de_equipos.csv"

# Si el archivo no existe, escribe los títulos
if not os.path.exists(archivo):
    with open(archivo, "w") as f:
        f.write("FECHA,EQUIPO,SERIAL,UBICACION\n")

while True:
    print("\n--- NUEVO REGISTRO ---")
    
    # 2. Pedir los datos por teclado
    equipo = input("Nombre del equipo: ")
    ubicacion = input("Ubicacion: ")
    serial = input("Serial (Escribelo o pegalo): ")

    # 3. Preparar la fila
    fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    fila = f"{fecha},{equipo},{serial},{ubicacion}\n"

    # 4. Guardar (Sin errores de librerias)
    with open(archivo, "a") as f:
        f.write(fila)

    print("\n✅ Guardado en inventario_de_equipos")
    
    # 5. Preguntar si seguir (Aqui estaba tu error en la imagen 1271)
    opcion = input("\n¿Registrar otro? (s/n): ").lower()
    if opcion != "s":
        break

print("Proceso finalizado.")

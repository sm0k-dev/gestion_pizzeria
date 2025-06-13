#Libraries
import os, time, msvcrt
from functions import *
#MenuText
menu = """\n=== GESTIÓN DE PEDIDOS ===
1) Registrar nuevas pizzas disponibles para la venta.
2) Ver el catálogo de pizzas.
3) Realizar un pedido.
0) Salir del sistema."""
#MenuText
#Menu
while True:
    #Welcome - CleanScreen
    os.system('cls')
    print(menu)
    option = input("Ingrese opción (0-3): ")
    os.system('cls')
    #Welcome - CleanScreen
    #Options
    #Option_1: Registrar pizzas.
    if option == '1':
        pass
    #Option_1
    #Option_2: Ver catálogo pizzas.
    elif option == '2':
        pass
    #Option_2
    #Option_3: Realizar pedido.
    elif option == '3':
        pass
    #Option_3
    #Option_0: Salir del sistema.
    elif option == '0':
        print("...Saliendo del sistema...")
        time.sleep(1)
    #Option_0
    else:
        print("Error. Opción inválida.")
    #OptionEnd - KeyToContinue
    print("...Presione una tecla para volver al menú principal...")
    msvcrt.getch()
    #Options
#Menu

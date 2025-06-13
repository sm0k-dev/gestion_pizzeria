#Resources
pizzas = []
masas = ("Tradicional", "Delgada", "Borde de queso mozzarella", "Parmesan Crunch", "Masa Maestra")
#Resources

#Functions
#REGISTRAR_PIZZA
def registrar_pizza():

   #Welcome
    print("=== **REGISTRAR PIZZA** ===")

   #Identification
    #CodeID
    print("""\n== ASIGNAR CÓDIGO ==""")
    codigo = int(input("Ingrese el código: "))
    #CodeID
    #Name
    print("""\n== ASIGNAR NOMBRE ==""")
    nombre = input("Ingrese el nombre: ")
    #Name
   #Identification
    
   #Dough
    #DoughAvailable
    print("""\n== ASIGNAR TIPO DE MASA ==\nMASAS DISPONIBLES:""")
    for i in range(len(masas)):
        print(f"{i+1}. {masas[i]}")
    #DoughAvailable
    #DoughSelect
    seleccion_masa = int(input(f"Seleccione tipo de masa (1-{i+1}): "))
    masa = masas[seleccion_masa-1]
    #DoughSelect
   #Dough
    
   #Price
    print("\n== ASIGNAR PRECIO ==")
    precio = float("Ingrese el precio: ")
   #Price
    
   #Stock
    print("\n== ASIGNAR STOCK ==")
    stock = int("Ingrese stock disponible: ")
   #Stock
    
    pizza = {
        "codigo": codigo,
        "nombre": nombre,
        "masa": masa,
        "precio": precio,
        "stock": stock
    }
    pizzas.append(pizza)
    print("Pizza registrada correctamente.")
#REGISTRAR_PIZZA
    
#VER_CATÁLOGO
def ver_catalogo():
    if not pizzas:
        print("No hay pizzas en el catálogo.")
    else:
        for pizza in pizzas:
            print(f"""{"="*10}\nCódigo: {pizza['codigo']}
Nombre: {pizza['nombre']}
Masa: {pizza['masa']}
Precio: {pizza['precio']}
Stock: {pizza['stock']}""")
#VER_CATÁLOGO

#Functions
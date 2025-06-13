#Resources
pizzas = []
pedidos = []
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
    
    #Register
    pizza = {
        "codigo": codigo,
        "nombre": nombre,
        "masa": masa,
        "precio": precio,
        "stock": stock
    }
    pizzas.append(pizza)
    print("Pizza registrada correctamente.")
    #Register
#REGISTRAR_PIZZA
    
#VER_CATÁLOGO
def ver_catalogo():
    #Exist?
    if not pizzas:
        print("No hay pizzas en el catálogo.")
    #ShowList
    else:
        for pizza in pizzas:
            print(f"""{"="*10}\nCódigo: {pizza['codigo']}
Nombre: {pizza['nombre']}
Masa: {pizza['masa']}
Precio: {pizza['precio']}
Stock: {pizza['stock']}""")
    #ShowList
#VER_CATÁLOGO

#REALIZAR_PEDIDO
def realizar_pedido():
    #RequestCodeID
    codigo = int(input("Ingrese el código: "))

    #FindRequestedCodeID
    for pizza in pizzas:
        #IfFound
        if pizza['codigo'] == codigo:
            #PizzaInfo
            print(f"Nombre: {pizza['nombre']}, Stock disponbile: {pizza['stock']}")

            #RequestAmountToBuy
            cantidad = int(input("Cantidad a comprar: "))

            #ValidAmountToBuy
            if cantidad <= pizza['stock']:
                #DiscountStock
                pizza['stock'] -= cantidad

                #TotalPrice
                total = cantidad * pizza['precio']

                #Register
                pedido = {
                    "nombre": pizza['nombre'],
                    "cantidad": pizza['cantidad'],
                    "total": pizza['total']
                }
                pedidos.append(pedido)
                print(f"Compra realizada por ${total} CLP.")
                return
                #Register
            #InvalidAmountToBuy
            else:
                print("No hay suficiente stock.")
                return
    #NotFound
    print("Pizza no encontrada.")
#REALIZAR_PEDIDO
#Functions
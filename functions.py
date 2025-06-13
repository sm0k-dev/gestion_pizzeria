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
    codigo = validar_codigo_unico()
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
    seleccion_masa = validar_entero_positivo(f"Seleccione tipo de masa (1-{i+1}): ")
    masa = masas[seleccion_masa-1]
    #DoughSelect
    #Dough
    
    #Price
    print("\n== ASIGNAR PRECIO ==")
    precio = validar_precio()
    #Price
    
    #Stock
    print("\n== ASIGNAR STOCK ==")
    stock = validar_entero_positivo("Ingrese stock disponible: ")
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
    codigo = validar_codigo()

    #FindRequestedCodeID
    for pizza in pizzas:
        #IfFound
        if pizza['codigo'] == codigo:
            #PizzaInfo
            print(f"Nombre: {pizza['nombre']}, Stock disponbile: {pizza['stock']}")

            #RequestAmountToBuy
            cantidad = validar_entero_positivo("Cantidad a comprar: ")

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

#VER_PEDIDOS
def ver_pedidos():
    #Exist?
    if not pedidos:
        print("No hay pedidos registrados.")
    #ShowList
    else:
        for pedido in pedidos:
            print(f"""\nPizza: {pedido['nombre']}
Cantidad: {pedido['cantidad']}
Total pagado: {pedido['total']}""")
#VER_PEDIDOS
#Functions
            
#ErrorControls
#VALIDAR_CODIGO
def validar_codigo():
    while True:
        cod = input("Asigne código a la pizza: ")
        if cod.isdigit() and int(cod) >= 1:
            return int(cod)
        print("Error. El código debe ser un número entero mayor o igual a 1.")
#VALIDAR_CODIGO
        
#VALIDAR_CODIGO_UNICO
def validar_codigo_unico(codigo):
    while True:
        for pizza in pizzas:
            if pizza['codigo'] == codigo:
                print("Error: Ya existe una pizza con ese código.")
                return False
        return True
#VALIDAR_CODIGO_UNICO
    
#VALIDAR_PRECIO
def validar_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio > 0:
                return precio
        except:
            print("Error. Debe ingresar un número positivo válido.")
#VALIDAR_PRECIO:
            
#VALIDAR_ENTERO_POSITIVO
def validar_entero_positivo(mensaje="Ingrese un número: "):
    while True:
        num = input(mensaje)
        if num.isdigit() and int(num) > 0:
            return int(num)
        print("Error. Debe ingresar un número entero mayor a 0.")
#VALIDAR_ENTERO_POSITIVO
#ErrorControls
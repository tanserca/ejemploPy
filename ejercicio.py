import funciones as fn
op = 3
        
  
fn.limpia()

while op !=5:

    print("    Menu    ")
    print("*"*12)
    print("1. Calcular Iva")
    print("2. Descuento")
    print("3. Calculo IMC")
    print("4. Borrar Pantalla")
    print("5. Salir")
    op = int(input("Ingrese1 una opcion (1-5) :"))

    if op == 1:
        precio = int(input("Ingrese precio del Producto: "))
        print("El iva del producto es: ",fn.calculariva(precio))

    if op == 2:
        precio = int(input("Ingrese Precio del Producto: "))
        descuento = int(input("Ingrese el % del Descuento: "))
        fn.calculoDescuento(precio,descuento)
    
    if op == 3:
        peso = float(input("Ingreso su peso: "))
        estatura = float(input("Ingrese su estatura: "))
        fn.calcularIMC(peso,estatura)

    if op == 4:
        fn.limpia()

fn.limpia()

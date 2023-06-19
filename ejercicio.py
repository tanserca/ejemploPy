import os
op = 3

def limpia():
    os.system("Cls")

def calculariva(precio):
    return precio*0.16

def calculoDescuento(precio,descuento):
    totaldesc = (precio-(precio*descuento/100))
    print("El precio a pagar incluyendo el descuento de (",descuento,"%) es de: ",totaldesc)

def calcularIMC(peso,estatura):
    imc= (peso/(estatura**2))

    if imc < 18.5:
        print("Bajo Peso")
    
    if imc >= 18.5 and imc<24.9:
        print("Peso adecuado")
    
    if imc >= 25 and imc <29.9:
        print("SobrePeso")
    
    if imc >=30 and imc < 34.9:
        print("Obesidad Nivel 1")
    if imc >=35 and imc < 39.9:
        print("Obesidad Nivel 2")
    if imc >40:
        print("Obesidad Nivel 3")
        
    
limpia()
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
        print("El iva del producto es: ",calculariva(precio))

    if op == 2:
        precio = int(input("Ingrese Precio del Producto: "))
        descuento = int(input("Ingrese el % del Descuento: "))
        calculoDescuento(precio,descuento)
    
    if op == 3:
        peso = float(input("Ingreso su peso: "))
        estatura = float(input("Ingrese su estatura: "))
        calcularIMC(peso,estatura)

    if op == 4:
        limpia()

limpia()
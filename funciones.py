
def limpia():
    import os

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

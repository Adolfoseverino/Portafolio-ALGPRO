def CalcularPotencia(b,e):
    acumulado = 1
    while e > 0 :
        acumulado = acumulado * b
        e = e -1
    return acumulado
base = -1
exponente = -1
while base <= 0 or exponente <=0:
    base = int(input("inserte la base"))
    exponente = int(input("inserte exponente"))
    if base <=  0 or exponente <= 0:
        print ("solo positivos")
potencia = CalcularPotencia(base, exponente)
print (potencia)
   

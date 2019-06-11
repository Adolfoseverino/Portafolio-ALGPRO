def deci_base(primervalor,basedeseada):
    resultado = 0
    potencia = 1
    while primervalor != 0:
         residuo = primervalor % basedeseada
         
         resultado += potencia * residuo
         
         potencia *= potencia * potencia
         
         primervalor //= basedeseada
    return resultado



def base_deci(primervalor, baseorigen):
    contadorpoten = 0
    result = 0

    while primervalor != 0:
        result += baseorigen ** contadorpoten * (primervalor % 10)
        primervalor //= 10
        contadorpoten += 1

    return result

primervalor = int(input("digite el valor:" ))
baseorigen = int (input("digite la base origen"))
basedeseada = int (input("digite la base que desea"))

if baseorigen == 10:
    print (deci_base(primervalor, basedeseada))
elif (basedeseada == 10):
    print (base_deci(primervalor,baseorigen))
else :
    print ("no puedo convertir eso")

def sumaNumeros(num):
	numCadena=str(num)
	for i in numCadena:
		if len(numCadena)==1:
			return num
		elif len(numCadena)>1:
			numero1=num%10
			numero2=num/10
			return numero1+numero2
a = int(input("digite numeros: "))
print sumaNumeros(a)


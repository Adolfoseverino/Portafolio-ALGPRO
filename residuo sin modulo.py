p,q=1,0
Dividendo=int(input("Ingresa Dividendo"))
Divisor=int(input("Ingresa Divisor"))
if(Dividendo>=Divisor):
 while((Dividendo-Divisor)>=q):
  q=Divisor*p
  p=p+1
 print("El cociente es "+str(p)+" y el residuo es "+str((Dividendo-q)))
else:
 print("el denominador debe ser menor")

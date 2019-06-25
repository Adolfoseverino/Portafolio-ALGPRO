def contarvocales():
    voc=0
    for i in len(cad):
        if cad[i]=='a' or cad[i]=='e'or cad[i]=='i' or cad[i]=='o' or cad[i]=='u' or cad[i]=='A'or cad[i]=='E' or cad[i]=='I' or cad[i]=='O'or cad[i]=='U':
            voc=voc+1
            return voc


cad = int(input("digite una palabra "))
print contarvocales(cad)

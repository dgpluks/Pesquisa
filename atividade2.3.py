a = float(input())
b = float(input())
c = float(input())
if a == 0 and b == 0 and c == 0:
    print("Igualdade confirmada: 0 = 0\n")
elif a == 0 and b == 0:
    print("Coeficientes informados incorretamente\n")
elif a == 0:
    print("Esta é uma equação de primeiro grau\n")
else: 
    print("Esta é uma equação de segundo grau\n")
    disc = b**2- 4*a*c
    if disc == 0:
        print("Esta é uma equação de segundo grau. Esta equação possui duas raízes reais iguais: x' = x'' = ",(b*-1)/(2*a))
    elif disc > 0:
        print("Esta é uma equação de segundo grau. Esta equação possui duas raízes reais diferentes: delta = ",disc ,", x' =" ,    round((-b+disc**(1/2))/(2*a),2),", x'' = ",round((-b-disc**(1/2))/(2*a),2))
    else:
        print("Esta é uma equação de segundo grau. Esta equação não possui raízes reais (delta < 0): delta = ", round(disc))

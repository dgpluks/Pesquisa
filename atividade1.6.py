rodas = 0
qn = -1
while qn < 0 or rodas < 0 or (rodas < qn*2 or rodas > qn * 4) or rodas % 2 == 1:
    qn = int(input("Digite a quantidade de veiculos\n"))
    rodas = int(input("Digite a quantidade de rodas"))
    if qn < 0 or rodas < 0 or (rodas < qn*2 or rodas > qn * 4) or rodas % 2 == 1:
        print("Algum valor está incorreto\n")
mts = 2*qn - rodas/2
car = qn - mts
print("Aquantidade de motos é ",mts,"e de carros é", car)

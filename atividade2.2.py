seq = [0] * 3
maior = 0
menor = 0
soma = 0
for i in range(3):
    seq[i] = int(input())
    if i == 0:
        maior = seq[i]
        menor = seq[i]
    if seq[i] > maior:
        maior = seq[i]
    if seq[i] < menor:
        menor = seq[i]
    soma += seq[i]
print("A media dos 3 é: ", soma/3, "O maior dos valores é : ", maior, "E o menor de todos é : ", menor)

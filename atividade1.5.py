v = [0] * 3 
soma = 0;
for i in range(3) :
    v[i] = int(input(f"digite o {i+1}° numero\n"))
    soma += v[i]
print(soma/3)

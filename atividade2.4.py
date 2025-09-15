val = int(input())
pag = int(input())
troc = val - pag
troco = [0] * 6 
nota = [50,20,10,5,2,1]
if(pag>val):
    print("valor pago é insuficiente\n")
else:
    for i in range(6):
        while troc >= nota[i]:
            troc = troc-nota[i]
            troco[i]+=1
    troc = 0
    for i in range(6):
        troc += troco[i]*nota[i]
        print("serão pagas ", troco[i], "notas de ", nota[i])
    print("Valor a ser pago é: ",  troc)

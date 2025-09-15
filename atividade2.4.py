val = int(input())
pag = int(input())
troc = val - pag
troco = [0] * 6 
if(pag>val):
    print("valor pago é insuficiente\n")
else:
    while(troc > 50):
        troc = troc-50
        troco[0]+=1
    while(troc > 20):
        troc = troc-20
        troco[1]+=1
    while(troc > 10):
        troc = troc-10
        troco[2]+=1
    while(troc > 5):
        troc = troc-5
        troco[3]+=1
    while(troc > 2):
        troc = troc-2
        troco[4]+=1
    while(troc >= 1):
        troc = troc-1
        troco[5]+=1
    troc = 0
    troc += troco[0]*50
    troc += troco[1]*20
    troc += troco[2]*10
    troc += troco[3]*5
    troc += troco[4]*2
    troc += troco[5]*1
    print(troc)


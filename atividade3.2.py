fat = int(input())
resp = 1;
while(fat < 0):
    print("Valor inválido, digite de novo\n")
    fat = int(input())
for i in range(1,fat+1):
    resp = resp *i
print(resp)

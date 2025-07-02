n = int(input())
bakery = [[]*3]*n
cst = (10**9)+1
for x in range(n):
    bakery[x]= list(map(int, input().split()))
    if bakery[x][0]<bakery[x][2]:
        cst = min(bakery[x][1], cst)

if cst == (10**9)+1: print(-1)
else: print(cst)
import math as meth

def coprimenikaal(x):
    yele = 0
    for i in range(x):
        if meth.gcd(i, x) == 1:
            yele +=1
    return yele

n = int(input())
ans = 0
for k in range(1, n+1):
    ans += (k%coprimenikaal(k))%(2**32)
print(ans)
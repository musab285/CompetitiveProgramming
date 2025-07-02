import math as meth
t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    ans = abs(n-k)
    cnt1=0
    cnt2= 0
    a= n
    b = k
    if n==k:print(0,0)
    else:
        while meth.gcd(a, b) != ans:
            a-=1
            b-=1
            cnt2+=1
        print(ans, cnt2)
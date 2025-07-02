t = int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    j=1
    k=2
    l=3
    fnd=False
    while i<n-3 and j<n-2 and k<n-1 and l<n and not fnd:
        if a[i]+a[j]!=a[k]+a[l]:fnd = True
        i+=1
        j+=1
        k+=1
        l+=1
    if fnd: print("YES")
    else: print("NO")
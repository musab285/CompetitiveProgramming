t= int(input())
for x in range(t):
    a,b = map(int,input().split())
    m = max(a, b)
    fnd = False
    while not fnd:
        if m%a==0 and m%b==0:
            fnd = True
        else: m+=max(a,b)
    print(m)
t = int(input())
for x in range(t):
    a,b,n,s = map(int,input().split())
    # if (a * n) + b < s:
    #     print("NO")
    # else: print("YES")
    anot = n
    bnot = 1
    fnd = False
    while anot<=a*n and bnot<=b and not fnd:
        if anot == s : fnd = True
        elif bnot == s: fnd = True
        elif anot + bnot == s : fnd = True
        if anot<=a*n:
            anot += n
        if bnot<=b:
            bnot += 1
    if fnd : print("YES")
    else: print("NO")
t = int(input())
for x in range(t):
    s1 = list(input())
    s2 = list(input())
    sorted(s1)
    sorted(s2)
    i= 0
    flg = True
    while i<len(s1) and flg:
        if s1[i] not in s2:
            flg = False
        i+=1
    if flg : print("YES")
    else: print("NO")

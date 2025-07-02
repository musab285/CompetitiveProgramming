t = int(input())
for x in range(t):
    n = int(input())
    s= input()
    i = 0
    tcnt= 0
    flg = False
    while i < n:
        j=i
        cnt = 0
        while j<n and not flg and s[j]==".":
            cnt+=1
            if cnt==3:flg = True
            j+=1
        if cnt!=0:
            i=j
            tcnt+=cnt
        else: i+=1
    if flg: print(2)
    else: print(tcnt)

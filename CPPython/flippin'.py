t = int(input())
s = list(map(int, input().split()))
i = 0
mx = 0
one = 0
mxcnt = 0
if t == 1:
    if s[0]==1:print(0)
    else:print(1)
else:
    while i<t:
        j= i
        cnt = 0
        if s[i] == 1:one +=1
        else:
            while j<t and s[j]==0:
                cnt+=1
                j+=1
        if cnt>0:i=j
        else: i+=1
        if mx==cnt:mxcnt+=1
        mx = max(mx, cnt)
    if mxcnt>1:
        print((mx*mxcnt)+one-1)
    else:
        print(mx+one)
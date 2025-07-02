t = int(input())
vwls = ['a', 'e', 'i', 'o', 'u']
for x in range(t):
    n = int(input())
    s = input()
    cnt = 0
    i = 0
    while i<n and cnt < 4:
        if s[i] not in vwls:
            cnt+=1
        else:
            cnt = 0
        i+=1
    if cnt >= 4 : print("NO")
    else: print("YES")
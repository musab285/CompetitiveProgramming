t = int(input())
for x in range(t):
    n = int(input())
    s = list(map(int, input()))
    cnt = 0
    i = 0
    out = []
    while i<n and cnt <2:
        if s[i]%2==1:
            out.append(s[i])
            cnt +=1
        i+=1
    if cnt == 2:
        print("".join(map(str, out)))
    else:
        print(-1)



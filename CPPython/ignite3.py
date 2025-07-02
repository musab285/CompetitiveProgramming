n = int(input())
a = []
for x in range(n):
    a.append(input())
q = int(input())
for x in range(q):
    s = input()
    cnt = 0
    s = sorted(s)
    for chk in a:
        nw = chk[:len(s)]
        nw =sorted(nw)
        if s == nw:
            cnt+=1
    if cnt == 0:
        print(-1)
    else:
        print(cnt)

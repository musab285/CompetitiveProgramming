t = int(input())
for x in range(t):
    n = int(input())
    s = sorted(list(map(int, input().split())))
    if len(set(s)) == 1:
        print(-1)
    else:
        b = [s[0]]
        c = []
        for i in range(1, n):
            if s[i] == b[0]:
                b.append(s[i])
            else:
                c.append(s[i])
        print(len(b), len(c))
        print(*b)
        print(*c)
t = int(input())
for x in range(t):
    n, m = map(int, input().split())
    cnt = 0
    length = 0
    for z in range(n):
        s = input()
        length+=len(s)
        if length > m :
            pass
        else:
            cnt += 1
    print(cnt)
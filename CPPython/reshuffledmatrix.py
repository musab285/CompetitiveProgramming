t = int(input())
for x in range(t):
    n, m = map(int, input().split())
    rows = [[]*m]*n
    col = [[]*n]*m
    for i in range(n):
        rows[i] = input()
    for i in range(m):
        col[i] = list(map(int, input().split()))
    for j in range(n):
        for i in range(m):
            print(col[i][j], end=" ")
        print()



n = int(input())
a = list(map(int, input().split()))
sm = 0
for i  in range(0, n, 2):
    sm += a[i]
print(sm)
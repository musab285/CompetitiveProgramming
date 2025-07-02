n, k = map(int, input().split())
x = list(map(int, input().split()))
x = sorted(x, reverse=True)
mx = 0
for i in range(k):
    mx += x[i]
print(mx)
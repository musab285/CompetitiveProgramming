t = int(int(input()))
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mn = min(a)
    if mn == a[0]:
        print("YES")
    else:
        print("NO")
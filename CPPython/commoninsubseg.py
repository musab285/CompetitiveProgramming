t= int(input())
for x in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k in a:
        print("YES")
    else:
        print("NO")
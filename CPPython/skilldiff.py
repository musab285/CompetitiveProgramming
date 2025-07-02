t = int(input())
for x in range(t):
    x,y,d = map(int, input().split())
    if abs(x-y) <= d:
        print("YES")
    else: print("NO")
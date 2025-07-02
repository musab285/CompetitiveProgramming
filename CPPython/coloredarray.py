t = int(input())
for x in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    if sum(s)%2==0:
        print("YES")
    else:
        print("NO")
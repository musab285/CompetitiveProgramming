t = int(input())
for x in range(t):
    n, m = map(int, input().split())
    if m>n:
        print("No")
    else:
        print("Yes")
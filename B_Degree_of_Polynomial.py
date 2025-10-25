t = int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mx = 0 
    for i in range(1, n):
        if a[i]!=0:
            mx = i
    print(mx)
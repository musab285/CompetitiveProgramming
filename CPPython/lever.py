t = int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 1
    for i in range(n):
        if a[i]>b[i]:
            cnt+=(a[i]-b[i])
    print(cnt)
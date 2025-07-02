n, x = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(n-1):
    if a[i] + a[i+1] > x:
        if a[i+1] == 0: chng = i
        else: chng=i+1
        cnt += (a[i] + a[i + 1]) - x
        a[chng] -= (a[i] + a[i+1]) - x
        if a[chng] < 0 : a[chng] = 0
print(cnt)
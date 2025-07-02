n, m = map(int, input().split())
a = list(map(int, input().split()))
x = [[]for i in range(n)]
sum = [0]*m
for i in range(n):
    x[i] = list(map(int, input().split()))
    for j in range(m):
        sum[j] += x[i][j]
flg = True
i=0
while flg and i<m:
    if sum[i]>=a[i]: flg = True
    else: flg=False
    i+=1
if flg: print("Yes")
else: print("No")

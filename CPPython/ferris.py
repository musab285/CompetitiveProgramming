n, x = map(int, input().split())
a= sorted(list(map(int, input().split())))
i = 0
j = n-1
cnt = 0
while i<j:
    if a[i]+a[j]>=x:
        cnt+=1
    i+=1
    j-=1
print(cnt)
n, k = map(int, input().split())
i = 1
cnt= 1
while i+k<=n:
    i+=1
    cnt+=1
print(cnt)
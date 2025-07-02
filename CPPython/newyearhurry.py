n, k = list(map(int, input().split()))
time = 240 - k
i = 1
cnt = 0
while time >= (i*5) and i<=n:
    time-=(i*5)
    cnt+=1
    i+=1
print(cnt)
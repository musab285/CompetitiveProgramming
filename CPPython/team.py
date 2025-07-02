t = int(input())
cnt = 0
for x in range(t):
    a = list(map(int, input().split()))
    if sum(a)>=2: cnt+=1
print(cnt)
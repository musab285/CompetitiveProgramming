n, p = map(int, input().split())
s = list(map(int, input().split()))
cnt=0
for _ in s:
    if _ < p:
        cnt+=1
print(cnt)
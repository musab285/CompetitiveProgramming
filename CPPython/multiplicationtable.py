n, x = map(int, input().split())
cnt = 0
for i in range(n):
    if x%(i+1)==0 and x//(i+1) <=n:
        cnt+=1
print(cnt)
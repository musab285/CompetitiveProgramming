n = int(input())
cnt = 0
mx = 0
while n!=0:
    crnt = n%2
    if crnt == 1:
        cnt+=1
    else:
        cnt = 0
    mx = max(cnt, mx)
    n = n//2
print(mx)
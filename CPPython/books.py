n, t = map(int, input().split())
s = list(map(int, input().split()))
cnt=0
# mxcnt = cnt
time = 0
i=0
j=0
while i< n:
    time += s[i]
    if time <= t:
        cnt+=1
    else:
        time-=s[j]
        j+=1
    i+=1
print(cnt)
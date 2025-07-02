n = int(input())
s = list(map(int, input().split()))
lwst = s[0]
high = s[0]
cnt=0
for i in range(1, n):
    if s[i] > high:
        high = s[i]
        cnt +=1
    elif s[i]<lwst:
        lwst = s[i]
        cnt+=1
print(cnt)
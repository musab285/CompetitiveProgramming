
n, k = map(int, input().split())
s = list(map(int, input().split()))
s=sorted(s)
lwst = 1000
for i in range(n):
    if k%s[i]==0 and (k/s[i])<lwst:
        lwst = k/s[i]
print(int(lwst))
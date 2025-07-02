n=int(input())
s = list(map(int, input().split()))
evncnt = 0
oddcnt = 0

for _ in s:
    if _%2 == 0: evncnt+=1
    else: oddcnt+=1
for _ in range(n):
    if oddcnt>evncnt:
        if s[_]%2==0:
            out = _+1
    elif evncnt>oddcnt:
        if s[_]%2!=0:
            out = _+1
print(out)
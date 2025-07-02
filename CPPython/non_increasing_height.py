n = int(input())
s = list(map(int, input().split()))
mx = max(s)
mn = min(s)
mxi=0
mni=0
fnd = False
i=0
while not fnd and i<n:
    if s[i] == mx:
        mxi=i
        fnd = True
    i+=1
i=n-1
fnd = False
while not fnd and i>=0:
    if s[i] == mn:
        mni=i
        fnd = True
    i-=1
out = mxi+((n-1)-mni)
if mxi>mni:
    out -= 1
print(out)
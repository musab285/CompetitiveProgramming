n = int(input())
x = list(map(int, input().split()))
sm = sum(x)
# print(sm)
i=n-2
crnt = x[n-1]
sm -= crnt
mndff = sm-crnt
while i>0:
    crnt+=x[i]
    sm -= x[i]
    if sm > crnt:
        mndff = min(mndff, sm - crnt)
    else:
        mndff = min(mndff, crnt-sm)
    i-=1
print(mndff)
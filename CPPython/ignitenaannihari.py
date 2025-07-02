n, d = map(int, input().split())
hlfn = n//2
if d==1:
    p = n+hlfn
    if p-n> 1:
        print(-1)
    else:
        print(p)
else:
    p = n-hlfn
    if n-p>1:
        print(-1)
    else:
        print(p)

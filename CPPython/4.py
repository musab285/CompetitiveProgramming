N , Q= map(int, input().split())
plyrs = [0]*N

for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        plyrs[x-1] += 1
    elif c == 2:
        plyrs[x-1] += 2
    else:
        if plyrs[x-1] >= 2:
            print("Yes")
        else:
            print("No")

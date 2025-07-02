t = int(input())
for x in range(t):
    l,r,d,u = map(int, input().split())
    lu = (u**2 + l**2)**0.5
    ur = (u**2 + r**2)**0.5
    dr = (d**2 + r**2)**0.5
    ld = (l**2 + d**2)**0.5
    lr = l+r
    ud = u+d
    if lu == ur == dr == ld and lr==ud:
        print("Yes")
    else: print("No")
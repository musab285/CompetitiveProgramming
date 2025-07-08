t= int(input())
for x in range(t):
    n, m, l, r = map(int, input().split())
    tm = n-m
    # ls = 0
    # rs = 0
    if l+tm<=0:
        l+=tm
    elif r-tm>=0:
        r-=tm
    else:
        tm += l
        l=0
        r-=tm
    print(l, r)
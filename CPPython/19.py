t = int(input())
while t:
    n = int(input())
    s = list(map(int, input().split()))
    print(s)
    if n==1: print(0)
    else:
        if sum(s)%n==0:
            scr=1
        else:
            scr= sum(s)//n
        print(scr)
    t-=1
t = int(input())
while t :
    n, x ,y = map(int, input().split())
    flag = False
    if x>=n:
        if (y/3)==n:
            flag = True
        else:
            n-=(y//3)
            x-=(y//3)
        n-=(x//2)
        if n>0:
            pass
        else: flag= True
    if flag: print('Yes')
    else: print("No")
    t-=1
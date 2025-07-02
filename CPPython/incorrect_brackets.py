t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    cnt=0
    strt=0
    for _ in s:
        if _ == "(":
            strt+=1
        else:
            strt-=1
            if strt<0:
                cnt+=1
                strt = 0
    print(cnt)
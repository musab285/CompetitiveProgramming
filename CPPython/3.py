t = int(input())
for i in range(t):
    n,m,s = map(int, input().split())
    temp = 0
    if m + (s-1) > n:
        while m + s > n:
            temp = n-(s-1)
            if m>temp:
                m-=temp
                s=out
                print(s)
            else:
                out = temp-m
                s=out
                print(s)
    else: out = s+(m-1)
    print(out)
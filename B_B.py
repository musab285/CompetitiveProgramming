n,m = map(int, input().split())
if m == 1:
    if n==1: print(1)
    else: print(2)

    for i in range(1, n+1):
        if i%2==0 : print(2)
        else: print(1)

else: 
    if n==1: print(2)
    else : print(4)

    a=1
    b=2
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j%2==0:
                print(b, end=" ")
            else: print(a, end=" ")
        if i%2==0:
            a-=2
            b-=2
        else: 
            a+=2
            b+=2
        print()





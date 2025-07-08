t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    if not n%2:
        print("No")
    else:
        if k>1:
            nm = int(str(n).join(str(n) for i in range(k-1)))
            print(nm)
        else:
            nm = n
        i = 2
        flg = True
        while flg and i<int(nm**0.5)+1:
            if nm % i != 0:
                flg = False
        # if flg:
        #     print(nm)
        # else:
        #     print(nm)
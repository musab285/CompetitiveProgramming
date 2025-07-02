t = int(input())
for x in range(t):
    n = int(input())
    a = list(input())
    flg = False

    lst = 0
    op = 0
    for i in range(n):
        if lst != a[i]:
            op +=2
        else:
            op+=1
        lst= a[i]
    print(op)



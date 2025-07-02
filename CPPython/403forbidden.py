n, m, q = map(int, input().split())
pgs = dict()
row = [False]*n
for x in range(q):
    a = list(map(int, input().split()))
    if a[0]==2:
        row[a[1]-1] = True
    elif a[0] == 1:
        pgs[(a[1]-1, a[2]-1)] = True
    else:
        # print(pgs)
        if row[a[1]-1]:
            print("Yes")
        elif (a[1]-1,a[2]-1) in pgs:
            print("Yes")
        else:
            print("No")
t = int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxsm= 0
    mxi = mxj = 0
    for i in range(n):
        for j in range(i+1, n):
             sum = 0
             nm = a[j]
             nm1 = a[i]
             prod = nm1*nm
             while prod > 0:
                 sum += prod%10
                 prod = prod//10
             maxsm = max(maxsm, sum)
    print(maxsm)

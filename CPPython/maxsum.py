t= int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mxsum = sum(a)
    # print(mxsum)
    i = 0
    while i<n-1:
        a[i] = a[i]*(-1)
        a[i+1] = a[i+1]*(-1)
        # print(a[i])
        # print(a[i+1])
        sm = sum(a)
        mxsum = max(sum(a), mxsum)
        if sm != mxsum:
            a[i] = a[i] * (-1)
            a[i + 1] = a[i + 1] * (-1)
        i+=2
    print(mxsum)
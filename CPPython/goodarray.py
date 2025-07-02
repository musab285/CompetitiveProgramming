t = int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pos = a.count(1)
    nig = a.count((-1))
    sm = sum(a)
    i = 0
    cnt= 0
    if sm >= 0 and nig%2==0 : print(0)
    else:
        while i<n and (sm<0 or nig%2!=0):
            if a[i] < 0:
                a[i] = abs(a[i])
                cnt +=1
                nig -= 1
                pos += 1
            # print(a)
            sm = sum(a)
            i+=1
            # print(a)
        print(cnt)
t = int(input())
for x in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0
    i = 0
    j = 0
    while i<n and j<m:
        print("a", a[i])
        print("b", b[j])

        if b[j]<=a[i]:
            cnt+=1
            j+=1
            print(cnt)
        i+=1
    # print(cnt)
    if cnt == m:
        print(0)
    elif m-cnt==1:
        print(b[j-1])
    else:
        print(-1)
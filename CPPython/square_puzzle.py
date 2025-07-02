t = int(input())
while t:
    n = int(input())
    s = list(map(int, input().split()))
    lyr = 1
    cnt = 0
    sum =  1
    sums = [1]
    while sum<=10000:
        sum+=lyr*8
        sums.append(sum)
        lyr+=1
    sum = 0
    for _ in s:
        sum+=_
        if sum in sums:
            cnt+=1
    print(cnt)
    t-=1
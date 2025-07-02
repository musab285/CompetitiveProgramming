t = int(input())
while t:
    n = int(input())
    s = list(input())
    i=0
    cnt = 0
    maxi = cnt
    one_cnt = 0
    while i<n:
        if s[i] == "0":
            while i<n and s[i] == "0":
                cnt +=1
                i+=1
        else:
            i+=1
            one_cnt +=1
        maxi = max(cnt, maxi)
        cnt = 0

    print(maxi+one_cnt)
    t-=1
t = int(input())
for x in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    people = 0
    cnt = 0
    i= 0
    while i<n:
        people+= s[i]
        if people >= m:
            cnt+=1
            people = 0

        else:
            while people<m and i<n-1:
                i+=1
                people += s[i]
            if people >= m:
                cnt += 1
                people = 0
        i+=1
    print(cnt)
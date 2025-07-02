t= int(input())
for x in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    cnt = 0
    i=0
    while len(s) > 0 and i<len(s):
        j = i+1
        while i<len(s) and j<len(s) and len(s)>0:
            if s[i]+s[j] == k:
                cnt+=1
                s.pop(j)
                s.pop(i)
                i-=1
                j-=1
            else :
                j+=1
        i+=1

    print(cnt)
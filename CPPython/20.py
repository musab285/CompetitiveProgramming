t = int(input())
while t:
    n = int(input())
    s = list(map(int, input().split()))
    i = 0
    j = 1
    while len(s)!=1:
        if i>=len(s):
            j=i
            while i>= len(s):
                i-=1
        else:
            i = j+1
            if j>=len(s):
                while j>=len(s):
                    j-=1
        s.append((s[i]+s[j])//2)
        s.pop(i)
        s.pop(j)

    print(s[0])
    t-=1
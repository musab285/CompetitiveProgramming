t = int(input())
for x in range(t):
    cnt=0
    s = input()
    fnd = False
    for i in range(len(s)):
        if s[i] == "1":
            if fnd:
                cnt+= (i-lst)-1
            lst = i
            fnd = True
    print(cnt)
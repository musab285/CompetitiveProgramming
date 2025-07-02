t = int(input())
while t:
    s = input()
    i= len(s)-1
    if i == 0 :
        print(0)
    else:
        fnd = False
        while not fnd and i>-1:

            if s[i]!='0':
                fnd = True
            else:
                i-=1
        cnt = len(s)-1-i
        for x in range(1,i+1):

            if s[x]!='0':
                cnt+=1
        print(cnt)
    t-=1




t = int(input())
for x in range(t):
    s = list(input())
    ln = len(s)
    t0 = s.count('0')
    if t0 == ln:
        print(0)
    else:
        x0 = 0
        i = 0
        while i<ln and s[i]!='1':
            x0+=1
            i+=1
        i= ln-1
        while i>-1 and s[i]!='1':
            t0-=1
            i-=1
        print(t0-x0)
t= int(input())
for x in range(t):
    s = input()
    i = 0
    flg = True
    while flg and i<len(s)-1:
        if s[i] == 'A' and s[i+1] == 'A' : flg = False
        elif s[i] == 'B' and s[i+1] == 'B': flg = False
        i+=2
    if flg: print("yes")
    else: print("no")
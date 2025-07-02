t = int(input())
yes = "Yes"
for x in range(t):
    s = input()
    if s[0] in yes:
        lst = yes.index(s[0])
        flg = True
    else: flg=False
    i = 1
    while flg and i<len(s):
        if s[i] in yes:
            # print(yes.index(s[i]))
            if yes.index(s[i])-lst==1:
                lst = yes.index(s[i])
            elif yes.index(s[i]) == 0 and lst==2:
                lst = 0
            else:
                flg = False
        else: flg = False
        i+=1
    if flg: print("YES")
    else: print("NO")

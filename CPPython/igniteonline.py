c = input().lower()
s = input().lower()
crnt = 0
# qs = False
cnt = 0
strtarr = []
for x in range(len(c)):
    # print(x)
    # print("C: ", c[x], "S: ", s[crnt])
    if c[x] == s[crnt]:
        if crnt == 0:
            strt = x
        crnt+=1
    elif s[crnt] == '?':
        if crnt == 0:
            strt = x
        crnt+=1
        # qs = True
    else:
        crnt = 0
    if crnt == len(s):
        cnt += 1
        strtarr.append(strt)
        # qs = False
        crnt = 0
    # print(crnt)
print(cnt)
print(*strtarr)
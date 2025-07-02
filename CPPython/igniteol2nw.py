c = input().lower()
s = input().lower()
i = 0
cnt = 0
strtarr = []
while i<len(c):
    j = 0
    flg = True
    while j<len(s) and i+j<len(c) and flg:
        if c[i+j] == s[j] or s[j]=='?':
            j+=1
        else:
            flg = False
    if j==len(s) and flg:
        cnt+=1
        strtarr.append(i)
        i+=1
    else:
        i+=1
print(cnt)
# print(" ".join(str(x) for x in strtarr))
print(*strtarr)
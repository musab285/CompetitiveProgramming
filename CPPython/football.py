s= input()
flg = False
for i in range(0, len(s)):
    cnt = 1
    j = i+1
    while j<len(s) and s[j]==s[i]:
        cnt+=1
        j+=1
    if cnt>=7:
        flg = True
if flg:
    print("YES")
else:
    print("NO")

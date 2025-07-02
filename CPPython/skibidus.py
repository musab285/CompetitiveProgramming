t = int(input())
for i in range(t):
    s= input()
    n = len(s)
    flg = False
    for i in range(n-1):
        if s[i] == s[i+1]:
            flg = True
            break
    if not flg: print(n)
    else: print(1)

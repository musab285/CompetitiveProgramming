s = input()
x = "hello"
ix = 0
cnt = 0
while ix<5 and cnt < len(s):
    crnt = x[ix]
    if s[cnt] == crnt:
        ix+=1
    cnt+=1
if ix==5:
    print("YES")
else: print("NO")


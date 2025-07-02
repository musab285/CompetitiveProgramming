n = int(input())
s = list(map(int, input().split()))
flg = False
i=0
while not flg and i<n-2:
    if s[i] == s[i+1] == s[i+2]:
        flg = True
    i+=1
if flg : print("Yes")
else: print("No")
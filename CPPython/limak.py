n = int(input())
s = list(map(int, input().split()))
fnd = False
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if s[i]!=s[j]and s[j]!=s[k] and s[i]!=s[k]:
                if abs(s[i]-s[j]) and abs(s[j]-s[k]) and abs(s[i]-s[k]) <= 2:
                    fnd = True
if fnd : print("YES")
else: print("NO")
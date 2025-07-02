def exist(c1, c2):
    i = 0
    j= 0
    while i<len(c1) and j<len(c2):
        if c1[i] == c2[j]:j+=1
        i+=1
    if j==len(c2):return True
    else: return False

n, m = map(int, input().split())
p = [[] for i in range(n)]
for x in range(n):
    p[x] = list(map(int, input().split()))
i= 0
fnd = False
while i < n and not fnd:
    for j in range(n):
        if j!=i:
            if p[i][0]>=p[j][0]:
                ci = p[i][2:]
                cj = p[j][2:]
                if exist(cj, ci):
                    if p[i][1]<p[j][1] or p[i][0]>p[j][0]:
                        fnd = True
                        break
    i+=1
if fnd : print("Yes")
else: print("No")
from http.cookiejar import user_domain_match

n, m = map(int, input().split())
floors = [[]*m]*n
used = [[False] * m for _ in range(n)]
rmcnt = 0
for x in range(n):
    floors[x] = input()

for i in range(n):
    j = 0
    while j<m:
        if floors[i][j] == "." and not used[i][j]:
            rmcnt+=1
            used[i][j] = True
            cont = True
            k=j
            while cont and k>0:
                if (not used[i][k-1] and floors[i][k-1]=="."):
                    used[i][k-1] = True
                    z = i
                    contx = True
                    while contx and z>0
                        if (not used[z-1][k-1] and floors[z-1][k-1]=="."):
                            used[z-1][k-1] = True
                        else:
                    if i <(n-1) and (not used[i+1][j-1] and floors[i+1][j-1]=="."):
                        used[i+1][j-1] = True
                elif j < (m-1) and (not used[i][j+1] and floors[i][j+1]=="."):
                    used[i][j+1] = True
                    if i >0 and (not used[i-1][j+1] and floors[i-1][j+1]=="."):
                        used[i-1][j+1] = True
                    if i <(n-1) and (not used[i+1][j+1] and floors[i+1][j+1]=="."):
                        used[i+1][j+1] = True
                else: cont=False
        j+=1
for k in range(n):
    print(used[k])
print(rmcnt)
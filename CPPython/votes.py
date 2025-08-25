n, m = map(int, input().split())
s = [input() for _ in range(n)]
votes = []
for j in range(m):
    zr = 0
    on = 0
    for i in range(n): 
        if s[i][j]=='1': 
            on += 1
        else: 
            zr +=1
    if zr==0 or on==0: 
        votes.append('2')
    elif zr>on: 
        votes.append('1')
    else: 
        votes.append('0')
cnd = [0] * n
mx = -1
for j in range(m):
    if votes[j] == '2':
        for x in range(n): 
            cnd[x]+=1
            mx = max(cnd[x], mx)
    else: 
        for i in range(n):
            if s[i][j] == votes[j]:
                cnd[i]+=1
                mx = max(cnd[i], mx)
# print(mx)
for x in range(n): 
    if cnd[x]==mx:
        print(x+1, end=" ")
print()
    
# print(cnd)
        
        

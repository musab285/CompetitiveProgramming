n, x = map(int, input().split())
s = list(map(int, input().split()))
i=0
ti=-1
tj=-1
sum=False
while i<n and not sum:
    j = 0
    while j<n and not sum:
        if j!=i and s[i] + s[j] == x:
            sum = True
            ti= i
            tj=j
        j+=1
    i += 1
if ti==-1 or tj== -1: print(-1)
else: print(f"{ti+1} {tj+1}")
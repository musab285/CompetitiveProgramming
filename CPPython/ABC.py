s = input()
n=len(s)
cnt=0
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
           if j-i == k-j and s[i]=='A' and s[j]== 'B' and s[k]=='C':
               cnt+=1
print(cnt)
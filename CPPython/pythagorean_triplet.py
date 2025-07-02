d = int(input())
s = []
for x in range(d):
    s.append(int(input()))
flg = False
i=0
while not flg and i<d:
    j =0
    while not flg and j<d:
        k=0
        while not flg and k<d:
            if (s[i]**2) == (s[j]**2) + (s[k]**2):
                flg = True
            k+=1
        j+=1
    i+=1
if flg : print("TRUE")
else: print("FALSE")
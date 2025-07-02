t = int(input())
for x in range(t):
    n = int(input())
    lst = n+3
    out = []
    for i in range(n):
        out.append(lst)
        lst+=3
    for i in range(n-2):
        if (out[i+2]*3)%(out[i]+out[i+1])==0:
            out[i]+=1
    print(" ".join(map(str, out)))

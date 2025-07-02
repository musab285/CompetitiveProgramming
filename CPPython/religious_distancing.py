inp = [int(x) for x in input().split()]
n= inp[0]
m= inp[1]
mn = min(n, m)
s=[]
for i in range(mn):
    if mn == n:
        s.append("GB")
    else: s.append("BG")
if mn == n:
    for i in range(m-mn):
        s.append("G")
else:
    for i in range(n-mn):
        s.append("B")
print("".join(s))
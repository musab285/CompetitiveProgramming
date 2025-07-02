n = int(input())
a = list(map(int, input().split()))
eql = True
i=0
while eql and i<n-1:
    if a[i] != a[i+1]:
        eql = False
    i+=1
if eql : print(0)
else: print(max(a))
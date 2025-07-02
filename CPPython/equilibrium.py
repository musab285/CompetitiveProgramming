n = int(input())
frcx= 0
frcy= 0
frcz=0
for i in range(n):
    x, y, z = map(int, input().split())
    frcx+=x
    frcy+=y
    frcz+=z
if frcz + frcy + frcx == 0:
    print("YES")
else: print("NO")
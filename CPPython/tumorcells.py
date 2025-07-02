n = int(input())
a = []
area = 0
peri = 0
for x in range(n):
    a.append(list(map(int,input().split())))
for x in range(n):
    for z in range(n):
        if a[x][z] <= 50:
            area+=1
            if x==0 or z==0 or x==n-1 or z==n-1 or (a[x+1][z]>50 or a[x-1][z]>50 or a[x][z+1]>50 or a[x][z-1] > 50):
                peri+=1
print(area, end=" ")
print(peri,"\n")

n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
gem = 0
cst = 0
for i in range(n):
    if c[i]<=v[i]:
        gem+=v[i]
        cst += c[i]
print(gem - cst)
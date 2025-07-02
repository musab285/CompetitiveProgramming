n= int(input())
x = list(map(int, input().split()))
mx = -(10**9)-1
sm = 0
for i in range(n):
    sm = max(sm + x[i], x[i])
    mx = max(sm , mx)
print(mx)

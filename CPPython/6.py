N = int(input())
A = list(map(int, input().split()))
div = N//2
if N%2 == 0:
    tmp1 = A[div:N]
    tmp2 = A[:div]
else:
    tmp1 = A[div+1:N]
    tmp2 = A[:N - div]
print(abs(sum(tmp1)-sum(tmp2)))
N = int(input())
sum = 0
while N:
    a, b = map(int, input().split())
    for i in range(b, a-1, -1):
        sum+= i

    N-=1
print(sum)

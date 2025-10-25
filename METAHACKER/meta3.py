t = int(input())
for x in range(t):
    n, a, b = map(int, input().split())
    print(f"Case #{x+1}: ", end=" ")
    for i in range((2*n)-1): print(1, end=" ")
    print(b)

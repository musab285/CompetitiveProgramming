t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    if k>n:
        print(-1)
    else: 
        for i in range(n-k):
            print(n-i, end=" ")
        for i in range(1, (n-k)+1):
            if i == n-k:
                print(i)
            else:
                print(i, end=" ")
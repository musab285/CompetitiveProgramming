t = int(input())
for i in range(t):
    psng = -1
    n , x = map(int, input().split())
    mrks = list(map(int, input().split()))
    mrks = sorted(mrks)
    print(mrks[n-x]-1)
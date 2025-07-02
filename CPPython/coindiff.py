t= int(input())
for x in range(t):
    n = int(input())
    v = sorted(list(map(int, input().split())))
    mn = abs(v[1]-v[0])
    for i in range(1, n-1):
        mn = min(abs(v[i]-v[i+1]), mn)
    print(mn)
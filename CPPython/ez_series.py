t = int(input())
for x in range(t):
    n,m,l,r = map(int, input().split())
    if abs(l)<r:
        low = int(l/n * m)
        high = m-abs(low)
    else:
        low = int(r / n * m)
        high = low - m
    print(f"{min(low, high)} {max(high, low)}")
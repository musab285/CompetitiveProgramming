t = int(input())
while t:
    l, r = map(int, input().split())
    if l and r != 1:
        print(abs(l-r))
    else: print(1)
    t-=1
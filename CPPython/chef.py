t = int(input())
for x in range(t):
    sx, sy, ex, ey = map(int, input().split())
    if sx!=ex and sy!=ey:print(1)
    else: print(2)

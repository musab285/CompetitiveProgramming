t = int(input())
for x in range(t):
    a,b,c = map(int, input().split())
    if a==b!=c:print(c)
    elif a==c!=b:print(b)
    elif c==b!=a:print(a)
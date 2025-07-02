t = int(input())
for x in range(t):
    n, s, t = map(int, input().split())
    if n == s == t:
        print(1)
    else:
        print((n-min(s, t))+1)
n, m = map(int, input().split())
s = input()
t = input()
if s==t:
    print(0)
elif s == t[:n]:
    if s == t[-n:] : print(0)
    else: print(1)
elif s == t[-n:] :
    print(2)
else:
    print(3)

t = int(input())
for i in range(t):
    x, y , z = list(map(int, input().split()))
    tm = x*y
    if x%3 == 0:
        brk = (x//3)-1
    else:
        brk = x//3
    brk = brk*z
    print(tm + brk)
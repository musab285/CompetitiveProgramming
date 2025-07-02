t=int(input())
for x in range(t):
    n = int(input())
    s = list(map(int, input()))
    one = sum(s)
    zero = n-one
    print(((n*one)+zero)-one)
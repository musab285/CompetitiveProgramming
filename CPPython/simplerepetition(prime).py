def primenikal(y):
    div = set()
    i=1
    while len(div)<=2 and i < int(y ** 0.5) + 1:
        if y % i == 0:
            div.add(i)
            div.add(y//i)
        i += 1
    return len(div) == 2

t = int(input())

while t:
    x, k = map(int, input().split())
    if x == 1 and k==2:
        print("YES")
    elif k==1 and primenikal(x):
        print("YES")
    else:
        print("NO")
    t-=1
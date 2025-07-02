d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

if y1 <= y2:
    if m1<=m2:
        if d1<=d2:
            print(0)
        else:
            print((d1-d2)*15)
    else:
        print((m1-m2)*500)
else:
    print(1000)
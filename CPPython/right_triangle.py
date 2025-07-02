x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

ab = (((x2-x1)**2) + ((y2-y1)**2))
ac = (((x3-x1)**2) + ((y3-y1)**2))
bc = (((x3-x2)**2) + ((y3-y2)**2))

if ab == ac + bc or bc == ac + ab or ac == ab + bc:
    print("Yes")
else:
    print("No")
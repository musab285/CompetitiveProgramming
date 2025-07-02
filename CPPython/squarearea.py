t = int(input())
for x in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    xi = min(x1, x2, x3, x4)
    xf = max(x1, x2, x3, x4)
    
    yi = min(y1, y2, y3, y4)
    yf = max(y1, y2, y3, y4)
    area = (abs(xi-xf))*(abs(yi-yf))
    print(area)
import math
t = int(input())
for x in range(t):
    y = int(input())
    d = (1+(8*y))
    if d <0:
        print("NAI")
    else:
        if math.isqrt(d) * math.isqrt(d) != d:
            print("NAI")
        else:
            n1 = ((2*y) + math.isqrt(d))/2
            n2 = ((2*y) - math.isqrt(d))/2
            n = max(n1, n2)
            # if n == int(n):
            #     print(n)
            # else:
            #     print("NAI")
            print(int(n))
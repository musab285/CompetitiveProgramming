t = int(input())
while t:
    n = int(input())
    sum = ((n*(1+((n**2)-((n-1)**2))))//2)
    print(sum%((pow(10, 9))+7))
    t-=1
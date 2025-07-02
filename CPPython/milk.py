n, x, y = map(int, input().split())
bttle = n
bottles = x*(n//y)
n -= (n-n%y)
bottles+=n
print(max(bottles, bttle))
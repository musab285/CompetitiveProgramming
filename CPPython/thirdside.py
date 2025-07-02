t = int(input())
for x in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    print(1+(sum(s)-n))

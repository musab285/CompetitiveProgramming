t = int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a)-min(a))
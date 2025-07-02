t = int(input())
for x in range(t):
    n = int(input())
    s = sorted(list(map(int, input().split())))
    mean = (s[0] + s[1]) // 2
    for i in range(2, n):
        mean = (mean+s[i])//2
    print(mean)
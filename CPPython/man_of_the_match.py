t = int(input())
while t:
    max = 0
    for i in range(22):
        r, w = map(int, input().split())
        if r+(w*20) > max:
            max = r+(w*20)
            j=i
    print(j+1)
    t-=1
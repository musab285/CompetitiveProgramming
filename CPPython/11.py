t = int(input())
while(t):
    n, x, k = map(int, input().split())
    s = input()
    zero=0
    ix=0
    for j in range(k):
        if ix >= n:
            break
        else:
            if s[ix] == 'L':
                x-=1
            else:
                x+=1
            if x==0:
                zero+=1
                ix = 0
            else:
                ix += 1
    print(zero)
    t-=1
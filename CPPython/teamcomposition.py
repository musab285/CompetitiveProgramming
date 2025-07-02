t = int(input())
for x in range(t):
    a, b = map(int, input().split())
    if a==0 or b==0:
        print(0)
    elif a+ b < 4:print(0)
    else:
        mn = min(a, b)
        mx = max(a, b)
        if mn == 1 and mx>=3: print(1)
        else:
            if mx //3 >= mn : print(mn)
            elif mx//2>=mn//2 : print(mn//2)
            else: print(0)

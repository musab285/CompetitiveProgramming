t = int(input())
for x in range(t):
    n = input()
    if int(n)%2 == 0:
        print(0)
    else:
        flg = True
        i = 0
        if int(n[0])%2==0:print(1)
        else:
            while i < len(n) and flg:
                if int(n[i])%2==0:
                    flg = False
                    break
                i+=1
            if not flg : print(2)
            else:
                print(-1)
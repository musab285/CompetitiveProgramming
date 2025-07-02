t = int(input())
for x in range(t):
    n = int(input())
    s = input()
    serv = "A"
    acnt = 0
    bcnt= 0
    for _ in s:
        if _ == serv:
            if _ == "A": acnt+=1
            else: bcnt+=1
        else: serv = _
    print(f"{acnt} {bcnt}")

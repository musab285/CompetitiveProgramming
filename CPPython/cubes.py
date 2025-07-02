t = int(input())
for x in range(t):
    n, f, k = map(int, input().split())
    cbs = list(map(int, input().split()))
    chck = cbs[f-1]
    # print(chck)
    grtcnt = 0
    smcnt = 0
    for _ in cbs:
        # print(_)
        if _ > chck: grtcnt+=1
        elif _ == chck: smcnt+=1
    # print(grtcnt, smcnt)
    if grtcnt>=k:
        print("NO")
    elif (smcnt-1)+grtcnt>=k:
        print("MAYBE")
    else:
        print("YES")

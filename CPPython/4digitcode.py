t=int(input())
for x in range(t):
    s = input()
    scnds = 0
    crsr = 1
    for _ in s:
        if int(_)!=0 and (crsr == 0 or crsr > int(_)):
            if crsr == 0:
                scnds += ((10-int(_)))+1
            else:
                scnds += (crsr-int(_))+1
        elif int(_)==0:
            if crsr==0:scnds+=1
            else: scnds+=(10-crsr)+1
        else:
            scnds+=(int(_)-crsr)+1
        crsr = int(_)
    print(scnds)

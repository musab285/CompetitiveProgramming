t = int(input())
for z in range(t):
    x= int(input())
    s= input()
    carl = 0
    chef = 0
    for _ in s:
        if _ == "C":carl+=2
        elif _=="N": chef+=2
        else:
            carl +=1
            chef+=1
    if carl>chef:
        print(60*x)
    elif chef>carl:
        print(40*x)
    else: print(55*x)
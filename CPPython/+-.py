t = int(input())
for x in range(t):
    n = int(input())
    s = list(input())
    pls = 0
    mns = 0
    for _ in s:
        if _ == "+":pls+=1
        else: mns +=1
    print(abs(pls - mns))
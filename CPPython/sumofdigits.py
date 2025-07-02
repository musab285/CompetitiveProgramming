def sum(s: object) -> object:
    sm = 0
    for _ in s:
       sm+=int(_)
    return str(sm)

n = input()
if len(n)==1:
    print(0)
else:
    cnt=1
    n = sum(n)

    while len(n)>1:
        n = sum(n)
        cnt+=1
    print(cnt)
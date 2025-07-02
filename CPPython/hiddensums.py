x = list(map(int, input().split()))
chck = max(x)
n=1
for _ in x:
    if _ != chck:
        if n==3:print(chck-_)
        else:print(chck - _, end= " ")
        n+=1

s, t = map(int, input().split())
a = 1
b = 2
c = 3
cnt = 0
while a+b+c <= s:
    if a*b*c <= t:
        cnt +=3
        a+=3
        b+=3
        c+=3
    else:
        a+=1
        b+=1
        c+=1
print(cnt)
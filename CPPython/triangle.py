b, a = map(int,input().split())
c = (2*a)//b
while (c*b)*0.5 < a:
    c+=1
print(c)
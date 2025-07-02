a,b = map(str, input().split())
n=1
flg = False
ln = min(len(a), len(b))
if ln == len(a):
    b = reversed(b)
else:
    a = reversed(a)
print(ln)
i=ln-1
while i>0 and not flg:
    if int(a[i])+int(b[i])>9:
        flg = True
        print(a[i],b[i])
        print(i)
    i-=1
if flg :
    print("Hard")
else:print("Easy")
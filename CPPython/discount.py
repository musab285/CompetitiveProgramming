n, d = map(int, input().split())
arr = list(map(int, input().split()))
sum=0
a = (n//(d+1))+1
while (n>0):
    x = 0
    for i in range(a):
        x+= arr[i]
    for i in range(a):
        arr.pop(0)

    sum += round(x, -1)
    d-=1
    n-=a
    if d>0:
        a=(n//(d+1))+1
    else:
        a=n
print(sum)
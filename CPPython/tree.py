n, m = map(int, input().split())
nm = n*m
mx = nm
ls = 1
i=0
arr = []
while i<nm:
    arr.append(mx)
    if mx != ls:
        arr.append(ls)
    mx-=1
    ls+=1
    i+=2
print(arr)
swap = True
for k in range(len(arr)-1):

    while swap:
        if k-1 >= 0:
            if abs(arr[k]-arr[k-1]) >=1:
                swap = False
            else: swap = True
        elif abs(arr[k]-arr[len(arr)-1]) >=1:
            swap = False
        else: swap = True
        if k+1 <= (len(arr)-1):
            if abs(arr[k]-arr[k+1])>=1:swap=False
            else: swap = True
        elif abs(arr[k]-arr[0]) >=1:swap= False
        else: swap=True
        if k-m>=0:
            if abs(arr[k]-arr[k-m]) >=1:swap= False
            else: swap=True
        if k+m<=(len(arr)-1):
            if abs(arr[k]-arr[k+m]) >=1:swap= False
            else: swap=True

        temp = arr[k]
        arr[k] = arr[k+1]
        arr[k+1] = temp
if swap:
    print(-1)
else: print(arr)
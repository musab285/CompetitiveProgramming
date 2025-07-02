n= int(input())
a = list(map(int, input().split()))
i = 0
flg = False
while i<n and not flg:
    nxt = a[i]-1
    nxt = a[nxt]-1
    if i+1 == a[nxt]:
        flg = True
    i+=1
flg and print("YES")
not flg and print("NO")
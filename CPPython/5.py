n,m = map(int, input().split())
a = input().split()
b = input().split()

cnt = 0
for i in range((m-n)+1):
    flag = True
    temp = b[i:i+n]
    for j in range(n):
        if a[j] == temp[j]: flag = False
    if flag:
        cnt+=1
print(cnt)
n = int(input())
a = list(map(int, input().split()))
mn = a[0]
cnt = 0
# while(mn>0):
#     i = 0 
#     flg = True
#     while(i < n and flg):
#         if a[i] % mn != 0:
#             flg = False
#         i += 1
#     if flg:
#         cnt += 1
#     mn -= 1

dv = set()
for i in range(1, int(mn**0.5) + 1):
    if mn % i == 0:
        dv.add(i)
        dv.add(mn // i)
dv = list(sorted(dv))
flg = True
i = len(dv) - 1
while i >=0  and flg:
    j = 0 
    while j < n:
        if a[i] % dv[i] == 0:
            flg = False
        j += 1
    if not flg:
        cnt += len(dv) - i
        break    
    else: 
        i += 1

print(cnt)
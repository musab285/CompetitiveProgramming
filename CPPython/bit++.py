n = int(input())
cnt = 0
for i in range(n):
    x = input()
    if '+' in x:
        cnt+=1
    else:
        cnt-=1
print(cnt)
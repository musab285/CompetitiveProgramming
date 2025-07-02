t = int(input())
for x in range(t):
    n = int(input())
    a = input()
    b = input()
    cnt = 0
    for i in range(n):
        if a[i] != b[i]:
            cnt = 1
            break
    if cnt == 1:
        print("YES")
    else:
        if a.count('1')%2==1 or b.count('1')==1:
            print("YES")
        else: print("NO")
t = int(input())
for x in range(t):
    n = int(input())
    s = input()
    i=0
    while s[i]=="W":
        i+=1
    # print(i)
    j = n-1
    cnt = 0
    while s[j]=="W":
        j-=1
        cnt +=1
    # print(cnt)
    mx = cnt+i
    print(n-mx)
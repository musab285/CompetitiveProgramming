t = int(input())
while t:
    s = input()
    i=0
    mx_cnt = 0
    while i < (len(s)-1):
        if s[i] != s[i+1]:
            i+=1
            mx_cnt +=1
        i+=1
    print(mx_cnt)
    t-=1
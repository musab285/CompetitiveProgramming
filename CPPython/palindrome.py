t = int(input())
for x in range(t):
    s = input()
    n = len(s)-1
    i = 0
    flg = True
    while flg and i<n:
        if s[i] != s[n-i]:
            flg = False
        i+=1
    flg and print("yes")
    not flg and print("no")
t = int(input())
for x in range(t):
    s = list(input())
    p = int(input())
    wght = 0
    ln = len(s)
    i=0
    news = ""
    while i<ln:
        # print(ord(s[i]))
        wght += ord(s[i])-96
        if wght > p:
            wght -= ord(s[i])-96
            ln-=1
            news = s[:i-1]
        print(wght)
        i+=1
    for _ in news:
        print(_, end="")
    print()
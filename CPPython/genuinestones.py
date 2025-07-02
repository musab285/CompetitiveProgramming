t= int(input())
for x in range(t):
    riyal = input()
    given = input()
    i = 0
    cnt = 0
    while i<len(riyal) and i<len(given):
        if riyal[i] in given: cnt +=1
        i+=1
    print(cnt)
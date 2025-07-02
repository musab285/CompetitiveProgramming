t = int(input())

for x in range(t):
    out = []
    n = input()
    for i in range(len(n)):
        chck = int(n[i])
        if chck >0:
            out.append(chck*(10**((len(n)-1)-i)))
    for _ in out:
        print(_, end=" ")
    print()
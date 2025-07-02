t = int(input())
for x in range(t):
    s = list(input())
    for j in range(len(s)-1, -1, -1):
        if s[j] == "p":s[j]="q"
        elif s[j] == "q":s[j]="p"
    print("".join(s[i] for i in range(len(s)-1, -1, -1)))
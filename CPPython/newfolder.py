n = int(input())
s = {}
for x in range(n):
    si = input()
    if si in s:
        s[si]+=1
    else:
        s[si]=0
    if s[si] == 0:
        print(si)
    else:
        print(si+f"({int(s[si])})")
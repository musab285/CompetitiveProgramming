t = int(input())
s = input()
T=0
A=0
for _ in range(t):
    if s[_] == 'T':
        T+=1
    else:
        A += 1

if A==T:
    if s[t-1]=='T':
        print("A")
    else:
        print("T")
else:
    if A>T: print("A")
    else: print("T")
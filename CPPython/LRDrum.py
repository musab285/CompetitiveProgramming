t= int(input())
for x in range(t):
    s1 = input()
    s2 = list(input())
    n = len(s2)
    i=0
    while i<n-1:
        if s2[i]==s2[i+1]:
            s2.pop(i+1)
            n-=1
        i+=1
    if list(s1)==s2:
        print("YES")
    else:
        print("NO")

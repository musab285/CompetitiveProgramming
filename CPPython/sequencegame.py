
t = int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    out = [a[0]]

    i = 1
    cnt = 0
    while i < n:
        if a[i-1]<= a[i]:
            out.append(a[i])
        else:
            out.append(1)
            out.append(a[i])
        i+=1
    print(len(out))
    print(" ".join(map(str, out)))

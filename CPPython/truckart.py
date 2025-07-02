n = int(input())
s = list(map(int, input().split()))
for crnt in range(n):
    ans = 1
    for i in range(n):
        if i!=crnt:
            ans*=s[i]
    if crnt < n-1:
        print(ans, end=" ")
    else: print(ans, end="")
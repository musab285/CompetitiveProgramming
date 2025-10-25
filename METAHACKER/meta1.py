t = int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if(n==1): 
        print(f"Case #{x+1}: {0}")
    else:
        mx = abs(a[0]-a[1])
        for i in range(1, n-1):
            mx = max(abs(a[i]-a[i+1]), mx)
        print(f"Case #{x+1}: {mx}")


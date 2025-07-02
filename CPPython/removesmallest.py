t = int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if i!=j and abs(a[i]-a[j])<=1:
                if a[i]<a[j]:
                   a.pop(i);
                else:
                    a.pop(j)
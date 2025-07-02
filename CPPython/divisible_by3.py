t = int(input())
while t:
    sum=0
    n = int(input())
    x = list(map(int, input().split()))
    for _ in x:
        sum+=_
    if sum%3 ==0:
        print("Yes")
    else:
        print("No")
    t-=1
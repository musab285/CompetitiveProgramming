t = int(input())
for x in range(t):
    a, b,c = map(int, input().split())
    if a==b:
        if c%2==1:
            print("First")
        else:print("Second")
    elif a>b:print("First")
    else:
        print("Second")

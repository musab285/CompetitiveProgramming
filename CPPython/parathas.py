t = int(input())
for x in range(t):
    a, b = map(int, input().split())
    if (a%2==0 and b%2==0) or (a%2==1 and b%2==1):
        print("Bob")
    else:
        print("Alice")
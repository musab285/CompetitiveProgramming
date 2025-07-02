t= int(input())
for x in range(t):
    n = int(input())
    if n==1:
        print(0)
    elif n==6:
        print(1)
    elif n==3:
        print(2)
    elif n>6 and n%36==0:
        print()
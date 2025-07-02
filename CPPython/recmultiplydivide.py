def rec(n):
    if n==1:return n
    elif n%2==0:
        n=n/2
        print(n)
    else:
        n=(n*3)+1
        print(n)

x = int(input())
print(rec(x))
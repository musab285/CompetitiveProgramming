def rec(k):
    if k==0:
        return 1
    else: return k*rec(k-1)

n = int(input())
print(rec(n))

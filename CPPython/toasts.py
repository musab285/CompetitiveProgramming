n, k, l, c, d, p, nl, np = map(int, input().split())
drnk = (k*l)//nl
slc = (c*d)
slt = p//np
print(min(drnk, slc, slt)//n)
a, b, x,y = map(int, input().split())
tele1 = min(x, y)
tele2 = max(x, y)
strt = min(a, b)
end = max(a, b)
if strt>tele1 :
    if abs(end - strt) > abs(end - tele2):
        dist = abs(strt-tele1) + abs(end-tele2)
    else:
        dist = abs(end - strt)
else:
    dist = abs(end - strt)
print(dist)
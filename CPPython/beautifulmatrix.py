a = []
for x in range(5):
    a.append(list(map(int, input().split())))
    for i in range(5):
        if a[x][i] == 1:
            ix = x+1
            ij = i+1
cnt = abs(3-ix) +abs(3-ij)
print(cnt)

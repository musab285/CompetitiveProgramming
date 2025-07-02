n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
end = n
for i in range(n):
    for j in range(i, end):
        if i!=j and s[i][0] >= s[i][1]:
            s[i], s[j] = s[j], s[i]
        elif s[i][1]>=s[j][1]:
            s[i], s[j] = s[j], s[i]
        elif s[i][2]>=s[j][2]:
            s[i], s[j] = s[j], s[i]
    end-=1
    if i>end:
        break
for i in range(n):
    print(*s[i])
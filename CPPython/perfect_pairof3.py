n, d = map(int, input().split())
s = list(map(int, input().split()))
cnt = 0
for i in range(7):
    for j in range(i+1, 7):
        for k in range(j+1, 7):
            if abs(s[k] - s[j]) == abs(s[j] - s[i]) and abs(s[k] - s[j])== d:
                cnt+=1
print(cnt)
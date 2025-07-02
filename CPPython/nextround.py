n , k = map(int, input().split())
s = list(map(int, input().split()))
scr = s[k-1]
cnt = 0
for _ in s:
    if _ >= scr:
        cnt+=1
print(cnt)
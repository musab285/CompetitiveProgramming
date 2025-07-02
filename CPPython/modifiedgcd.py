a, b = map(int, input().split())
div = set()
for i in range(1, int(max(a, b)**0.5)+1):
    if b%i==0 and a%i==0:
        div.add(i)
        m = max(a, b)
        n = min(a, b)
        if m%(n//i) == 0:
            div.add(m//i)
        elif n%(m//i) == 0:
            div.add(n//i)
# print(div)
div = sorted(div)
n = int(input())

for i in range(n):
    l, h = map(int, input().split())
    j = 1
    mx = 0
    while j<len(div) and div[j]<=h:
        if div[j]>=l:
            mx = max(div[j], mx)
        j+=1
    if mx == 0:print(-1)
    else: print(mx)
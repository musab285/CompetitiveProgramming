n,pos, l, r= map(int, input().split())
cnt = 0
if abs(pos-r)>abs(pos-l):
    if l>1:
        cnt+=(abs(pos-l))+1
        pos = l
    if r<n:
        cnt+=(abs(r-pos))+1
else:
    # if l>1:
    #     cnt+=(abs(pos-l))+1
    #     pos = l
    if r < n:
        cnt += (abs(r - pos)) + 1
        pos = r
    if l>1:
        cnt+=(abs(pos-l))+1

print(cnt)
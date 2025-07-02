n = int(input())
s = input()
pos = 0
cnt = 0
for _ in s:
    if _ == "U":
        if pos + 1 == 0:
            cnt+=1
        pos+=1
    else:
        pos-=1
print(cnt)
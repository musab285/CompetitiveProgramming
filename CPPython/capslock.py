s = list(map(str, input()))
for i in range(len(s)):
    if i==0:
        print(s[i].upper(), end="")
    else:
        print(s[i].lower(), end="")

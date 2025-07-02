s = list(map(str, input()))
nws = ""
vwls = ['a', 'e', 'i', 'o', 'u', 'y']
for i in range(len(s)):
    if s[i].lower() not in vwls:
        nws += "."
        nws += s[i].lower()
print(nws)

s = input()
nws = ""
for i in range(1, len(s)):
    nws+=s[i]
if nws.isupper():
    nws = nws.lower()
print(s[0].upper()+nws)
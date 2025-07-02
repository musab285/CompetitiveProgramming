a, b = map(int, input().split())
chck = a/b
if (int(chck)+1)-chck > (int(chck)-chck):
    print(int(chck))
else:
    print(int(chck)+1)
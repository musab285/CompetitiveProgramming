t= int(input())
for x in range(t):
    s = input()
    if len(set(s)) == 1:
        print(-1)
    else:
        print(len(s) - 1)
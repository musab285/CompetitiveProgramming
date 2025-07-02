t = int(input())
for x in range(t):
    s = input()
    t = input()
    if len(t)>len(s):
        print(len(t)+1)
    elif len(t)==len(s):
        print(len(t)+len(s))
    else:
        print(len(s)+1)
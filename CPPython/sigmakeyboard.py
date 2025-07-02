s= input()
out = []
for _ in s:
    if _ != "B":
        out.append(_)
    elif len(out)>0:
        out.pop()
for _ in out:
    print(_, end="")
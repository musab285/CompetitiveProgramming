def divs(n):
    div = set()
    for i in range(int(n**0.5), 0,-1):
        if n%i==0:
            div.add(n//i)
            div.add(i)
    return sorted(list(div))

n = int(input())
div = divs(n)
for _ in div:
    print(_)
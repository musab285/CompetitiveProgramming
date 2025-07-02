def divs(n):
    div = set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            div.add(n//i)
            div.add(i)
    return len(div)
n = int(input())
for x in range(n):
    u, l = map(int, input().split())
    mx = u-1
    mxcnt = 0
    for i in range(u, l+1):
        div = divs(i)
        if div>mxcnt:
            mxcnt=div
            mx = i
    print(f"Between {u} and {l}, {mx} has a maximum of {mxcnt} divisors.")

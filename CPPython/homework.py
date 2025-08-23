t = int(input())
for x in range(t):
    n = int(input())
    a = input()
    m = int(input())
    b = input()
    x = input()
    vld = ""
    dma = ""
    for i in range(m):
        if(x[i]=='V'):
            vld += b[i]
        else:
            dma += b[i]
    print(f"{vld[::-1]}{a}{dma}")

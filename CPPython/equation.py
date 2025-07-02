a, b, c = map(int, input().split())
d= (b**2) - 4*(a*c)
if a==0 and b==0 and c ==0:
    print(-1)
elif a==0 and b == 0:
    print(0)
elif d<0:
    print(0)
elif a==0:
    out1 = format(-c/b, ".10f")
    print(1)
    print(out1)
else:
    out1 = ((-b)+(d)**0.5)/(2*a)
    out2 = ((-b)-(d)**0.5)/(2*a)
    out1 = out1
    out2 = out2
    if out1 == out2 :
        print(1)
        print(out1)

    else:
        print(2)
        print(f"{min(out1, out2):.10f}")
        print(f"{max(out1, out2):.10f}")


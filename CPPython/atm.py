x, y = map(float, input().split())
if x == 0 :print(f"{y:.2f}")
elif x % 5 == 0:
    if x>y or ((y - x) - 0.5) < 0:
        print(f"{y:.2f}")
    else:
        print(f"{(y - x) - 0.5:.2f}")
else:
    print(f"{y:.2f}")
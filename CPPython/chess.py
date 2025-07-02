a,b = input().split()
if (int(a[-1])%2==0 and int(b[-1])%2==0) or (int(a[-1])%2!=0 and int(b[-1])%2!=0):
    print("Black")
else: print("White")
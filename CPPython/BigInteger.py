n = int(input())
if n>= -128 and n < 128:
    print("byte")
elif n>= -32768 and n<32768:
    print("short")
elif n>=-2147483648 and n<2147483648:
    print("int")
elif n>=-9223372036854775808 and n<9223372036854775808:
    print("long")
else:
    print("BigInteger")
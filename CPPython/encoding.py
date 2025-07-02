t= int(input())
for x in range(t):
    n = int(input())
    s = input()
    i = 0
    out = ""
    while i<n-1:
        if s[i] == '0' and s[i+1] == '0' : out+="A"
        elif s[i] == '0' and s[i+1] == '1': out+="T"
        elif s[i] == '1' and s[i + 1] == '0': out += "C"
        elif s[i] == '1' and s[i + 1] == '1':
            out += "G"
        i+=2
    print(out)
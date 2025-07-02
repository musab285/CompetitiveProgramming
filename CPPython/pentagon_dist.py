i1 = input()
i2 = input()

x = {"A":1, "B":2 , "C":3, "D":4, "E":5}

def dis(p,q):
    return min(abs(x[p] - x[q]), 5-abs(x[p] - x[q]))

if dis(i1[0], i1[1])==dis(i2[0], i2[1]):
    print("Yes")
else: print("No")

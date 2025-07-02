hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
n = int(input())
out =""
if n == 0: out =  "00"
while n > 0:
    out = out+hexa[n%16]
    n = n//16
    if n == 0 and len(out)<2: out = out + "0"
result = ""
for i in range(len(out)-1, -1, -1):
    result = result + out[i]
print(result)
keys = "qwertyuiopasdfghjkl;zxcvbnm,./"
move = input()
s = input()
result = ""
for _ in s:
    if move == "R":
        i = keys.find(_)-1
        if i<0:
            result += keys[len(keys)-1]
        else: result += keys[i]
    else:
        i = keys.find(_)+1
        if i > len(keys)-1:
            result += keys[0]
        result += keys[i]
print(result)
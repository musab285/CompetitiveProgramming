n, t = map(int, input().split())
s = list(input())
for i in range(t):
    index = 0
    while index < n-1:
        if s[index] == 'B' and s[index+1] == 'G':
            temp = s[index]
            s[index] = s[index+1]
            s[index + 1] = temp
            index+=2
        else:
            index+=1
for x in s: print(x, end="")
n = int(input())
first = input()
grp = 1
for x in range(n-1):
    y = input()
    if y!=first:
        grp +=1
    first = y
print(grp)
n = int(input())
x = [[]for i in range(n)]
j = [[]for z in range(n)]
for i in range(n):
    x[i] = list(map(int, input().split()))
    for k in range(n):
        if x[i][k] == 1:
            j[i].append(k+1)
for i in range(n):
    for z in range(len(j[i])):
        print(j[i][z], end=" ")
    print()
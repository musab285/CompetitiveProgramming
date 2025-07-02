n = int(input())
arr = []
for x in range(1, n+1):
    arr.append(x)
print(max(arr), end =" ")
for x in range(len(arr)-1):
    print(arr[x], end=" ")
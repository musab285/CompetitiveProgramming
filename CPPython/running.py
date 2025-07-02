t = int(input())
for x in range(t):
    n = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    cnt=0
    for i in range(n):
        if alice[i]/bob[i] <=2 and bob[i]/alice[i]<=2:
            cnt+=1
    print(cnt)
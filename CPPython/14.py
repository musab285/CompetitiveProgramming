t = int(input())
while(t):
    sum =0
    sumy=0
    sumx=0
    s = input()
    sum = int(s[3]) + int(s[2]) + int(s[0]) + int(s[1])
    sumy = int(s[3]) + int(s[2])
    sumx= int(s[0]) + int(s[1])
    sumx*=10
    sumy*=10
    sum*=10
    print((sumx*sumy)+ sum +1)
    t-=1
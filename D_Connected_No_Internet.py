t,s,x = map(int, input().split())

if x<t:print("NO")
elif t==x: print("YES")
elif (x-t)%s==0 and (x-t)!=0 or (x-t)%s==1 and (x-t-1)!=0: print("YES")
else: print("NO")
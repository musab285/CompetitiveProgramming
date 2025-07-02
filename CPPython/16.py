dik , era = map(int, input().split())
cnt = 1
flag = True
while dik and era>=cnt and flag:
    dik -= cnt
    cnt+=1
    if era<cnt:
        print("Valera")
        flag = False
    era -= cnt
    cnt+=1
if flag:
    print("Vladik")
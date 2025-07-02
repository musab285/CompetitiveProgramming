def find(s1, s2):
    if len(s1)<len(s2):return "No"
    else:
        i=0
        while i< len(s1):
            cnt = 0
            j= i
            while j<len(s1) and cnt<len(s2) and (s1[j]=='?' or s1[j]==s2[cnt]):
                # print(s1[j])
                # print(s2[cnt])
                cnt+=1
                j+=1

            if cnt>=len(s2):return "Yes"
            i+=1
        return "No"
incrct = input()
crct = input()
print(find(incrct, crct))

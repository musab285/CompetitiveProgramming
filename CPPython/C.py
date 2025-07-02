s = ["Asad", "Foyj", "Juwel", "Mijan", "Tanmay"]
n = list(map(int, input()))
for _ in n:
    if _<=5:
        print(s[_-1])
    else:
        mltple = _//5
        newi = _-((5*mltple)+mltple+1)
        print(s[newi])
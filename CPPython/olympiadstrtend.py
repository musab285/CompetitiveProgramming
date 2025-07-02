h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())

hrs = h2-h1
if m2<m1:
    hrs-=1
    mins = 60-(m1-m2)
else:
    mins = m2-m1
if s2<s1:
    mins-=1
    scnds = 60-(s1-s2)
else:
    scnds = s2-s1
print(hrs, mins, scnds)

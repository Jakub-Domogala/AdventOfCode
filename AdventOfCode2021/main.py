c = {}
c[1] = True
c[2] = True
c[3] = True
print(c)
for i in c:
    c[i+10] = True
print(c)
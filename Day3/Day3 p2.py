lines = []
with open('Day3.txt', 'r') as l:
    lines = l.readlines()

oxynumber = lines
conumber = lines
temptrue = []
tempfalse = []

for n in range(12):
    for oxy in oxynumber:
        if oxy[n] == '1':
            temptrue.append(oxy)
        else:
            tempfalse.append(oxy)
    if len(temptrue) >= len(tempfalse):
        oxynumber = temptrue
    else:
        oxynumber = tempfalse
    temptrue = []
    tempfalse = []
    if len(oxynumber) == 1:
        break




for n in range(12):
    for co in conumber:
        if co[n] == '0':
            temptrue.append(co)
        else:
            tempfalse.append(co)
    if len(temptrue) <= len(tempfalse):
        conumber = temptrue
    else:
        conumber = tempfalse
    temptrue = []
    tempfalse = []
    if len(conumber) == 1:
        break


print(oxynumber[0])
print(conumber[0])
oxynumber = int(oxynumber[0], 2)

conumber = int(conumber[0], 2)
print(oxynumber)
print(conumber)
print(conumber*oxynumber)




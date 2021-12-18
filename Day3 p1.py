lines = []
with open('Day3.txt', 'r') as l:
    lines = l.readlines()

gamma = []
epsilon =[]
n = 0
one = 0
zero = 0

for n in range(12):
    for line in lines:
        if line[n] == '1':
            one += 1
        else:
            zero += 1

    if one > zero:
        gamma.append('1')
    else:
        gamma.append('0')
    n =+ 1
    one = 0
    zero = 0

for i in gamma:
    if i == '1':
        epsilon.append('0')
    else:
        epsilon.append('1')

epsilonnr = int(''.join(epsilon), 2)
gammanr = int(''.join(gamma), 2)

print( gammanr*epsilonnr)
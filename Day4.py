plansze = [[]]
losy = []
with open('Day4exe.txt', 'r') as l:
    losy = l.readlines()[0].replace('\n', '')

losy = losy.split(',')
print(losy)
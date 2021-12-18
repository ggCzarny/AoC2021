lst = [("aaaa8"),("bb8"),("ccc8"),("dddddd8")]
#print([s.strip('8') for s in lst]) # remove the 8 from the string borders
#print([s.replace('8', '') for s in lst]) # remove all the 8s 

lines = []
with open('Day3.txt', 'r') as l:
    lines = l.readlines()

lines = s.replace('\n', '') for s in lines
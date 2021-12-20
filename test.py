
value = []
size_y = 5
size_x = 5

for i in range(size_x):
    row = []
    for j in range(size_y):
        row.append(0)
    value.append(row)



def create_map(cords, map):
    for cord in cords:
        #map[cord[0], cord[1]] += 1
        map[cord[0]][cord[1]] += 1
        print(map[0][0])


cords = [(1, 3), (2, 4), (1, 3)]

result = create_map(cords, value)

for x in value:
    print(x)
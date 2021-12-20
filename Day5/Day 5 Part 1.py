
class VentLines:
    def __init__(self, lines):
        self.values = []
        for line in lines:
            line = line.replace('\n', '')
            line = line.replace(' -> ', ',')
            line_values = [int(number) for number in line.split(',')  if number != "\n" and number != ""]
            if line_values[0] == line_values[2] or line_values[1] == line_values[3]: self.values.append(line_values)
    
    def get_points_of_line(self):
        cords = []
        points = self.values
        for point in points:
            x1 = point[0]
            y1 = point[1]
            x2 = point[2]
            y2 = point[3]
            if x1 == x2:
                for i in range(max([y1, y2]) - min([y1, y2]) + 1):
                    x = x1
                    y = min([y1,y2])+i
                    cords.append((x, y))
            if y1 == y2:
                for i in range(max([x1, x2]) - min([x1, x2]) + 1):
                    y = y1
                    x = min([x1,x2])+i
                    cords.append((x, y))
        return cords

class OceanMap:
    def __init__(self, lines):
        self.value = []
        all_x = []
        all_y = []
        for value in VentLines(lines).values:
            all_x.append(value[0])
            all_x.append(value[2])
            all_y.append(value[1])
            all_y.append(value[3])
        self.size_x = max(all_x)
        self.size_y = max(all_y)
        for i in range(self.size_y+1):
            self.row = []
            for j in range(self.size_x+1):
                self.row.append(0)
            self.value.append(self.row)
    
    def create_map(self, cords):
        result = self.value[:]
        for cord in cords:
            result[cord[1]][cord[0]] += 1
            
        return result


with open('Day5/input.txt', 'r') as f:
    lines = [line for line in f.readlines() if line != "\n"]
    result = OceanMap(lines).create_map(VentLines(lines).get_points_of_line())
    for line in result:
        print(line)






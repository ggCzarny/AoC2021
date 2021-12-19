
class VentLines:
    def __init__(self, lines):
        self.values = []
        for line in lines:
            line = line.replace('\n', '')
            line = line.replace(' -> ', ',')
            line_values = [int(number) for number in line.split(',')  if number != "\n" and number != ""]
            if line_values[0] == line_values[2] or line_values[1] == line_values[3]: self.values.append(line_values)
    
    def get_points_of_line(points):
        cords = []
        x1 = points[0]
        y1 = points[1]
        x2 = points[2]
        y2 = points[3]
        if x1 == x2:
            for i in range(max([y1, y2]) - min([y1, y2]) + 1):
                x = x1
                y = min([y1, y2])+i
                cords.append((x, y))
        if y1 == y2:
            for i in range(max([x1, x2]) - min([x1, x2]) + 1):
                y = y1
                x = min([x1,x2])+i
                cords.append((x, y))
        return cords


with open('Day5/inputExe.txt', 'r') as f:
    lines = [line for line in f.readlines() if line != "\n"]
    print(VentLines(lines).values)
    for vent_line in VentLines(lines).values:
        print(VentLines.get_points_of_line(vent_line))



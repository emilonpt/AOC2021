import copy 
with open("./input.txt", encoding = 'utf-8') as f:
    data = [d for d in f.read().split('\n')]

"""data = [
"0,9 -> 5,9",
"8,0 -> 0,8",
"9,4 -> 3,4",
"2,2 -> 2,1",
"7,0 -> 7,4",
"6,4 -> 2,0",
"0,9 -> 2,9",
"3,4 -> 1,4",
"0,0 -> 8,8",
"5,5 -> 8,2"]
dim = 10"""
dim = 1000
plane1 = [[0 for y in range(dim)] for x in range(dim)] #note you access the x,y coordinates by plane1[y][x]


def get_ranges(line):
    line_x_start = int(line.split(',')[0])
    line_y_start = int(line.split(',')[1].split(' ')[0])
    line_x_end = int(line.split(' ')[2].split(',')[0])
    line_y_end = int(line.split(' ')[2].split(',')[1])

    if line_x_start <= line_x_end:
        lines_x_range = range(line_x_start, line_x_end + 1)
    else:
        lines_x_range = range(line_x_end, line_x_start + 1)[::-1] #order matters for diagonals!
    if line_y_start <= line_y_end:
        lines_y_range = range(line_y_start, line_y_end + 1)
    else:
        lines_y_range = range(line_y_end, line_y_start + 1)[::-1] #order matters for diagonals!

    return lines_x_range, lines_y_range

for line in data:

    lines_x_range, lines_y_range = get_ranges(line)

    #part 1 - consider only horizontal and vertical lines
    if len(lines_x_range) == 1:
        for y in lines_y_range:
            plane1[y][min(lines_x_range)] += 1 #note that the x-axis is selected by the y value
    if len(lines_y_range) == 1:
        for x in lines_x_range:
            plane1[min(lines_y_range)][x] += 1 #note that the y-axis is selected by the x value


#part 2 - consider diagonal lines as well

plane2 = copy.deepcopy(plane1)

for line in data:
    lines_x_range, lines_y_range = get_ranges(line)
    if len(lines_x_range) > 1 and len(lines_y_range) > 1:
        """for c,x in enumerate(lines_x_range):
            plane2[y][x] += 1"""
        x_list = [i for i in lines_x_range]
        y_list = [i for i in lines_y_range]
        xy_set = set(zip(x_list,y_list))
        for x,y in xy_set:
            plane2[y][x] += 1

flat_plane1 = [item for sublist in plane1 for item in sublist]
at_least_two_overlaps = len([i for i in flat_plane1 if i  >= 2])
print(at_least_two_overlaps)

flat_plane2 = [item for sublist in plane2 for item in sublist]
at_least_two_overlaps = len([i for i in flat_plane2 if i  >= 2])
print(at_least_two_overlaps)

'''for i in plane1:
    print(i)

print("---")'''

"""for i in plane2:
    print(i)"""
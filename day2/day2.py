
with open("./input.txt", encoding = 'utf-8') as f:
    data = [d for d in f.read().splitlines()]

'''data=[
"forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2"]'''

instructions =  []
for instruction in data:
    instructions.append({instruction.split(" ")[0]:instruction.split(" ")[1]})

#part 1

horizontal = 0
depth = 0

for d in instructions:
    x = list(d.keys())[0]
    if x == "down":
        depth += int(d[x])
    elif x == "up":
        depth -= int(d[x])
    elif x == "forward":
        horizontal += int(d[x])

print(horizontal*depth)

#part 2

horizontal = 0
depth = 0
aim = 0

for d in instructions:
    x = list(d.keys())[0]
    if x == "down":
        aim += int(d[x])
    elif x == "up":
        aim -= int(d[x])
    elif x == "forward":
        horizontal += int(d[x])
        depth += aim*int(d[x])

print(horizontal*depth)
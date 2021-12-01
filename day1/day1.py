#part 1
with open("./part1.txt", encoding = 'utf-8') as f:
    data = [d for d in f.read().splitlines()]

data = [int(d) for d in data]
counter = 0
for c,v in enumerate(data):
    if c > 0:
        if v>data[c-1]:
            counter += 1

print(counter)


#part 2
counter = 0
for c,v in enumerate(data):
    if c > 2 and c < len(data):
        if(sum(data[c-2:c+1])>sum(data[c-3:c])):
            counter += 1
print(counter)
#import copy
from collections import Counter
with open("./input.txt", encoding = 'utf-8') as f:
    data = [d for d in f.read().split('\n')]

data = [int(d) for d in data[0].split(',')]

#Part 1 before optimizations - not suitable for part 2
"""
def process_day(data):
    #Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.
    data_to_return = copy.deepcopy(data)
    for c,d in enumerate(data):
        if d == 0:
            data_to_return[c] = 6
            data_to_return.append(8)
        else:
            data_to_return[c] -= 1
    return data_to_return


def model_x_days(data, x):

    for i in range(x):
        print(i)
        data = process_day(copy.deepcopy(data))

    return data

#part1
#print(len(model_x_days(data, 80)))
"""
#re-work for part 2 to be more efficient (ie. not to wait "forever")

def process_day_v2(data_counts):
    num_zeroes = data_counts[0]
    for i in range(1,9):
        to_add = data_counts[i]
        to_subtract = data_counts[i-1]
        data_counts[i - 1]  += to_add
        data_counts[i - 1] -= to_subtract

    data_counts[6] += num_zeroes
    data_counts[8] = num_zeroes
    return data_counts

#data = "3,4,3,1,2"
#data = [int(d) for d in data.split(',')]
data_counts = Counter(data)

#part 1
for i in range(80):
    data_counts = process_day_v2(data_counts)

num_elements = sum(data_counts.values())

print(num_elements)

#part 2

data_counts = Counter(data)

for i in range(256):
    data_counts = process_day_v2(data_counts)

num_elements = sum(data_counts.values())

print(num_elements)
import copy
from collections import Counter
with open("./input.txt", encoding = 'utf-8') as f:
    data = [d for d in f.read().split('\n')][0]

#data = "16,1,2,0,4,2,7,1,2,14"

data = [int(d) for d in data.split(',')]
data = sorted(data)
#print(data)
data_median = data[len(data)//2]

#part 1

fuel_spent = sum([abs(d-data_median) for d in data])

print(fuel_spent)
"""
#part 2  - this is NOT WORKING for live input, but works for test
data_average = int(round(sum(data)/len(data),0))
#print(data_average)
fuel_spent = {d:sum([i for i in range(1,int(abs(d-data_average))+1)]) for d in data}

counts = Counter(data)

total_fuel_spent = {k:int(v*counts[k]) for k,v in fuel_spent.items()}

print(sum(total_fuel_spent.values()))
"""

#working part 2  - not using average - relatively slow but not too bad
total_fuel_spent = {}
counts = Counter(data)
print(counts)
for number in range(max(data)+1):
    distances = {k:abs(k-number) for k in set(data)}
    fuel_spent = {k:sum([i for i in range(1,int(abs(k-number))+1)]) for k in set(data)}
    total_fuel_spent[number] = sum([int(v*fuel_spent[k]) for k,v in counts.items()])

best_key = min(total_fuel_spent, key=total_fuel_spent.get)

print(total_fuel_spent[best_key])
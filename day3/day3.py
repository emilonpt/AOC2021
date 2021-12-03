with open("./input.txt", encoding = 'utf-8') as f:
    data = [d for d in f.read().splitlines()]

"""data=[
"00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"]"""

def cols_from_rows(rows):
    cols = [[] for b in rows[0]]

    for v in rows:
        for cc,vv in enumerate(v):
            cols[cc].append(vv)
    return cols

def find_most_and_least_common(col):
    most_common = max(set(col), key = col.count)
    least_common = min(set(col), key = col.count)
    return most_common, least_common

def to_decimal_and_multiply(x,y):
    return int(x,2)*int(y,2)

cols = cols_from_rows(data)
#part 1
gamma = ""
epsilon = ""
for col in cols:
    vals = find_most_and_least_common(col)
    gamma += vals[0]
    epsilon += vals[1]

print(to_decimal_and_multiply(gamma,epsilon))

#part 2

rows_oxygen = data.copy()
rows_CO2 = data.copy()

cols_oxygen = cols_from_rows(rows_oxygen)
cols_CO2 = cols_from_rows(rows_CO2)

def remove_rows_on_col_index(row,col_index,to_remove):
    to_return = row.copy()
    if len(row) > 1:
        for r in row:
            if r[col_index] == to_remove:
                to_return.remove(r)
    return to_return

def get_value(cols,c,rows,gas_type):
    if len(rows) == 1:
        return rows[0]
    most_common, least_common = find_most_and_least_common(cols[c])
    if most_common == least_common:
        if gas_type == "oxygen":
            least_common = "0"
        elif gas_type == "CO2":
            most_common = "1"
    if gas_type == "oxygen":
        rows = remove_rows_on_col_index(rows,c,least_common)
    elif gas_type == "CO2":
        rows = remove_rows_on_col_index(rows,c,most_common)
    cols = cols_from_rows(rows)
    return get_value(cols,c+1,rows,gas_type)


rows_oxygen = get_value(cols_oxygen,0,rows_oxygen,"oxygen")
rows_CO2 = get_value(cols_CO2,0,rows_CO2,"CO2")

print(to_decimal_and_multiply(rows_oxygen,rows_CO2))
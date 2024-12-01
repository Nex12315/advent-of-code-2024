with open('input.in', 'r') as file:
    left_column = []
    right_column = []

    for line in file:
        chars = line.split()
        left_column.append(int(chars[0]))
        right_column.append(int(chars[1]))

left_column.sort()
right_column.sort()
similarities = []

for el in left_column:
    similarities.append(el * right_column.count(el))

print(sum(similarities))

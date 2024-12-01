def calculate_difference(num1, num2):
    return max(num1, num2) - min(num1, num2)


with open('input.in', 'r') as file:
    left_column = []
    right_column = []

    for line in file:
        chars = line.split()
        left_column.append(int(chars[0]))
        right_column.append(int(chars[1]))

left_column.sort()
right_column.sort()
differences = []

for i in range(len(left_column)):
    differences.append(calculate_difference(left_column[i], right_column[i]))

print(sum(differences))

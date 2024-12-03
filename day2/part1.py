def check_for_safety(arr, is_decreasing):
    for i in range(len(arr) - 1):
        diff = arr[i] - arr[i + 1]

        if is_decreasing:
            if diff > 3 or diff <= 0:
                return 0
        else:
            if diff < -3 or diff >= 0:
                return 0
    return 1


with open('input.in', 'r') as file:
    sum_of_save = 0
    for line in file:
        arr_line = [int(x) for x in line.split()]
        sum_of_save += check_for_safety(arr_line, arr_line[0] > arr_line[1])


print(sum_of_save)

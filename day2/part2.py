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


def problem_dampener(arr):
    success_count = 0
    for i in range(len(arr)):
        modified_arr = arr.copy()
        modified_arr.pop(i)
        success_count += check_for_safety(
            modified_arr, modified_arr[0] > modified_arr[1]
        )
    if success_count > 0:
        return 1
    else:
        return 0


with open('input.in', 'r') as file:
    sum_of_save = 0
    for line in file:
        arr_line = [int(x) for x in line.split()]
        is_line_safe = check_for_safety(arr_line, arr_line[0] > arr_line[1])
        if is_line_safe == 1:
            sum_of_save += 1
        else:
            sum_of_save += problem_dampener(arr_line)

print(sum_of_save)

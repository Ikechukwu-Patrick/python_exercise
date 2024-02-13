def sum_first_middle_last(arr):
    length = len(arr)
    if length < 3:
        return "List should have at least 3 elements"
    else:
        return arr[0] + arr[length // 2] + arr[length - 1]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_first_middle_last(my_list)
print(result)



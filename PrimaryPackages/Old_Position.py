def sum_even_positions(lst):

    return sum(lst[1::2])


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_even_positions(my_list)
print(f"Sum of elements at even positions: {result}")

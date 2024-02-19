def third_element_adder(my_element):
    total = 0
    for i in range(2, len(my_element), 3):
        total = total + my_element[i]
    return total


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(third_element_adder(my_list))

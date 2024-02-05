def smallest_elements(list):
    numbers = list[0]
    for elements in list:
        if elements < numbers:
            numbers = elements
    return numbers

lists = [349,677,349,885,559,686]
print(smallest_elements(lists))



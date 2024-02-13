original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
subsequent_duplicate = []
for element in original_list:
    subsequent_duplicate.append(element)
    subsequent_duplicate.append(element)
    print('Here is the duplicated list as expected', subsequent_duplicate)

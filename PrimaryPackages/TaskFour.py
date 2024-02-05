def get_largest(numbers):
    largest = numbers[0]
    for elements in numbers:
        if elements > largest:
            largest = elements

    return largest

list = [1,2,5,4,8,9,7]
print(get_largest(list))
def count_letters_digits(input_string):
    letters = 0
    digits = 0

    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    return letters, digits


input_string = input("Enter a string: ")

letters, digits = count_letters_digits(input_string)

print("LETTERS", letters, "DIGITS", digits)


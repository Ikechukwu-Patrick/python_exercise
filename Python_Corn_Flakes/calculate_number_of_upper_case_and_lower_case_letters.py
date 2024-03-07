def calculate_number_of_upper_case_and_lower_case_letters(input_string):
    upper_case_letters = 0
    lower_case_letters = 0
    for letter in input_string:
        if letter.isupper():
            upper_case_letters += 1
            if letter.lower():
                lower_case_letters += 1
                return upper_case_letters


input_string = input("Enter a string: ")
upper_case_letters, lower_case_letters = calculate_number_of_upper_case_and_lower_case_letters(input_string)
print(upper_case_letters)


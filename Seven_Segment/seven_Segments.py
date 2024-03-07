def display_Number(numbers):
    if len(numbers) == 8:
        holder = list(numbers)

        if holder[7] == '1':

            if holder[0] == '1':
                print('#######')
            else:
                print()

            if holder[1] == '1':
                print('      #')
                print('      #')
            else:
                print()

            if holder[6] == '1':
                print('#######')

            # for _ in range(2):
            if holder[4] == '1':
                print('#     ')
                print('#     ')
            if holder[2] == '1':
                print('######')

            else:
                print('')

            if holder[3] == '1':
                print('########')
            else:
                print()


number = input('Enter any positive number:')
print(display_Number(number))

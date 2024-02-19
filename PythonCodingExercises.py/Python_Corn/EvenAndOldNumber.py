numbers = int(input('Enter any positive number '))
even = 0
old = 0
for i in range(1, numbers):
    if i % 2 == 0:
        even += i
    else:
        old += i
print("The sum of even numbers is ", even)
print("The sum of old numbers is", old)

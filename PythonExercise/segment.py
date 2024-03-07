# Define the segments for each number (0-9)
segments = {
    0: [1, 1, 1, 1, 1, 1, 0],
    1: [0, 1, 1, 0, 0, 0, 0],
    2: [1, 1, 0, 1, 1, 0, 1],
    3: [1, 1, 1, 1, 0, 0, 1],
    4: [0, 1, 1, 0, 0, 1, 1],
    5: [1, 0, 1, 1, 0, 1, 1],
    6: [1, 0, 1, 1, 1, 1, 1],
    7: [1, 1, 1, 0, 0, 0, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1]
}


# Function to display a number on a seven segment display
def display_number(num):
    if num < 0 or num > 9:
        print("Invalid number")
        return

    segments_on = segments[num]

    for i, segment in enumerate(segments_on):
        if segment:
            print(" # ")
        else:
            print("#   #")

        if i == 0 or i == 3 or i == 6:
            print("#")


display_number(5)

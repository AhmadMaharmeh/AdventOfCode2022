# Import the input.txt file
data = open('input.txt', 'r').read().split('\n')

# Make an int for total sum
total_sum = 0

# Make a dictionary with the priority scores
priority = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}

# Remove the last empty element
data.pop()

# Create an empty list to store the new parsed data
# Every 3 lines will be broken up and put into elements/subelements
my_list = [list(group) for group in zip(data[0::3], data[1::3], data[2::3])]

# Iterate through the list
for element in my_list:
    
    # Make a list for char of first subelement
    first_char = []

    # Make a list for char of second subelement
    second_char = []

    # Make a list for char of third subelement
    third_char = []

    # Iterate through the characters of the first subelement
    for char in element[0]:
        first_char.append(char)
    for char in element[1]:
        second_char.append(char)
    for char in element[2]:
        third_char.append(char)

    # Convert them into sets
    set1 = set(first_char)
    set2 = set(second_char)
    set3 = set(third_char)
    
    common_elements = list(set1.intersection(set2, set3))

    # Access the value of the dict based on the common element
    value1 = priority.get(common_elements[0])

    total_sum = total_sum + value1

print(total_sum)


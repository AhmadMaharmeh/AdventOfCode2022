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

# Remove the last blank element in the list
data.pop()

# Iterate through the list
for element in data:
    # Split the string into two halves
    half_length = int(len(element)/2)
    half1 = element[0:half_length]
    half2 = element[half_length:len(element)]
    
    # Make a list for half1 char
    half1_char = []

    # Make a list for half2 char
    half2_char = []

    # Iterate through the characters of half1
    for char in half1:
        half1_char.append(char)
    # Iterate through the characters of half2
    for char in half2:
        half2_char.append(char)
        
    # Convert the lists to sets
    set1 = set(half1_char)
    set2 = set(half2_char)

    common_elements = list(set1.intersection(set2))

    print(common_elements)
    # Access the value of the dict based on the common element
    value1 = priority.get(common_elements[0])

    total_sum = total_sum + value1


print(total_sum)

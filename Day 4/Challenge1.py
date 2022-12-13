# Import the input.txt file
data = open('input.txt', 'r').read().split('\n')

# Remove the last empty element
data.pop()

# Make an empty int for total count
total_count = 0

# Split each string by the ',' character, then split each sub-element by the '-' character
# and then convert each element to an integer
my_list = [[[int(x) for x in y.split('-')] for y in z.split(',')] for z in data]

# Iterate through the list
for element in my_list:
    if element[0][0] >= element[1][0] and element[0][1] <= element[1][1]:
        total_count = total_count + 1
    elif element[1][0] >= element[0][0] and element[1][1] <= element[0][1]:
        total_count = total_count + 1

print(total_count)

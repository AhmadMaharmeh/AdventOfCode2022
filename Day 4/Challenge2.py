# Import the input.txt file
data = open('input.txt', 'r').read().split('\n')

# Remove the last empty element
data.pop()

# Make an empty int for total count
total_count = 0

# Split each string by the ',' character, then split each sub-element by the '-' character
# And then convert each element to an integer
my_list = [[[int(x) for x in y.split('-')] for y in z.split(',')] for z in data]

# Iterate through the list
for element in my_list:
    if min(element[1]) <= max(element[0]) and max(element[1]) >= min(element[0]):
        total_count = total_count + 1

print(total_count)

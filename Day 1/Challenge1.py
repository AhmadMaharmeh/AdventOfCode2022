# Advent of Code Day 1

# Import the input file
data = open('input.txt', 'r').read().split('\n')

elves = []

elf = []

max_sum = 0

# iterate over the list of strings and parse the numbers into a list of lists
for line in data:
    # if the line is not a blank line, add the number to the current Elf's list
    if line != "":
        elf.append(int(line))
    # if the line is a blank line, add the current Elf's list to the list of Elves and reset the current Elf's list
    else:
        elves.append(elf)
        elf = []

# iterate over the inner lists and calculate the sum of each one
for inner_list in elves:
    # calculate the sum of the current inner list
    sum = 0
    for number in inner_list:
        sum += number

    # update the maximum sum if the current sum is larger than the previous maximum
    if sum > max_sum:
        max_sum = sum

# print the maximum sum
print(max_sum)

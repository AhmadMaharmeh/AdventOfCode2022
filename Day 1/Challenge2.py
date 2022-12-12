# Advent of Code Day 1
import heapq

# Import the input file
data = open('input.txt', 'r').read().split('\n')

elves = []

elf = []

# initialize a list to store the sums of the largest numbers within each inner list
sums_of_largest_numbers = []

# iterate over the list of strings and parse the numbers into a list of lists
for line in data:
    # if the line is not a blank line, add the number to the current Elf's list
    if line != "":
        elf.append(int(line))
    # if the line is a blank line, add the current Elf's list to the list of Elves and reset the current Elf's list
    else:
        elves.append(elf)
        elf = []

# calculate the sum of each Elf's list of numbers
sums = [sum(elf) for elf in elves]

# use heapq.nlargest to get the 3 largest sums
largest_3_sums = heapq.nlargest(3, sums)

# print the largest 3 sums
print(largest_3_sums)
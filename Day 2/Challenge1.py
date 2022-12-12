# Import the input.txt file
data = open('input.txt', 'r').read().split('\n')

# Create an empty list to store the split elements
strategy = []

# Create an int equal to zero to keep tally of the total score
total_score = 0

# Iterate over the elements of the original list
for element in data:
    strategy.append(element.split(' '))

# Remove the last empty element in the list
strategy.pop()


# Symbols to RPS
# A = Rock
# B = Paper
# C = Scissors
# X = Rock
# Y = Paper
# Z = Scissors

# Possible outcomes
# Opponent: A Player: X  = Draw
# Opponent: A Player: Y = Win
# Opponent: A Player: Z = Lose
# Opponent: B Player: X = Lose
# Opponent: B Player: Y = Draw
# Opponent: B Player: Z = Win
# Opponent: C Player: X = Win
# Opponent: C Player: Y = Lose
# Opponent: C Player: Z = Draw

# Iterate over the elements of the list
for i in strategy:
    if i[0] == 'A' and i[1] == 'X':
        total_score = total_score + 1 + 3
    if i[0] == 'A' and i[1] == 'Y':
        total_score = total_score + 2 + 6
    if i[0] == 'A' and i[1] == 'Z':
        total_score = total_score + 3
    if i[0] == 'B' and i[1] == 'X':
        total_score = total_score + 1
    if i[0] == 'B' and i[1] == 'Y':
        total_score = total_score + 2 + 3
    if i[0] == 'B' and i[1] == 'Z':
        total_score = total_score + 3 + 6
    if i[0] == 'C' and i[1] == 'X':
        total_score = total_score + 1 + 6
    if i[0] == 'C' and i[1] == 'Y':
        total_score = total_score + 2
    if i[0] == 'C' and i[1] == 'Z':
        total_score = total_score + 3 + 3

print(total_score)

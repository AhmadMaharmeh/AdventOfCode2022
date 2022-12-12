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
# X = Lose
# Y = Draw
# Z = Win

# Possible outcomes
# Opponent: A Player: X = Lose (Pick Scissors)
# Opponent: A Player: Y = Draw (Pick Rock)
# Opponent: A Player: Z = Win (Pick Paper)
# Opponent: B Player: X = Lose (Pick Rock)
# Opponent: B Player: Y = Draw (Pick Paper)
# Opponent: B Player: Z = Win (Pick Scissors)
# Opponent: C Player: X = Lose (Pick Paper)
# Opponent: C Player: Y = Draw (Pick Scissors)
# Opponent: C Player: Z = Win (Pick Rock)

# Iterate over the elements of the list
for i in strategy:
    if i[0] == 'A' and i[1] == 'X':
        total_score = total_score + 3
    if i[0] == 'A' and i[1] == 'Y':
        total_score = total_score + 3 + 1
    if i[0] == 'A' and i[1] == 'Z':
        total_score = total_score + 6 + 2
    if i[0] == 'B' and i[1] == 'X':
        total_score = total_score + 1
    if i[0] == 'B' and i[1] == 'Y':
        total_score = total_score + 3 + 2
    if i[0] == 'B' and i[1] == 'Z':
        total_score = total_score + 6 + 3
    if i[0] == 'C' and i[1] == 'X':
        total_score = total_score + 2
    if i[0] == 'C' and i[1] == 'Y':
        total_score = total_score + 3 + 3
    if i[0] == 'C' and i[1] == 'Z':
        total_score = total_score + 6 + 1

print(total_score)

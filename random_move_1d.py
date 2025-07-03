import random

line = ['.', '.', '.', '.', '.']
dot_position = 2
line[dot_position] = 'D'
print(''.join(line))

# Clear old position
line[dot_position] = '.'

# Randomly pick a direction
direction = random.choice(['left', 'right'])

# Line length
line_length = len(line)

# Move the dot
if dot_position > 0 and direction == 'left':
    dot_position -= 1
elif dot_position < line_length -1 and direction == 'right':
    dot_position += 1

# Set new position
line[dot_position] = 'D'
print(''.join(line))




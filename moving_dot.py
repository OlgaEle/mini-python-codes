# 👣 A simple dot moving on a line

# Create a line with 5 positions
line = ['.', '.', '.', '.', '.']

# Set the initial position of the dot
dot_position = 3
line[dot_position] = 'A'

# Show the line
print(''.join(line))

# Clear the old position
line[dot_position] = '.'

# Move right
dot_position += 1

# Move left
dot_position -= 1

# Find the length of the line
line_length = len(line)

# Move the dot based on its current position
if dot_position < line_length - 1:
    # Move right
    dot_position += 1
elif dot_position == line_length - 1:
    # Move left
    dot_position -= 1

# Show the final position of the dot
line[dot_position] = 'F'

# Print the final line
print(''.join(line))

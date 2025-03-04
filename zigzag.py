def print_zigzag(s, k):
    if k == 1:
        print(s)
        return

    # Create a 2D list to store the zigzag pattern
    zigzag = [[' ' for _ in range(len(s))] for _ in range(k)]
    row = 0
    col = 0
    direction = 1  # 1 for down, -1 for up

    for char in s:
        zigzag[row][col] = char
        col += 1
        if row == 0:
            direction = 1
        elif row == k - 1:
            direction = -1
        row += direction

    # Print the zigzag form
    for line in zigzag:
        print(''.join(line))

# Example usage
s = "thisisazigzag"
k = 4
print_zigzag(s, k)
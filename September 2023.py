def find_first_sensible_row(tower):
    # Iterate through each row in reverse order
    for i in range(len(tower) - 1, -1, -1):
        # Check if the row is completely filled or empty
        if all(cell == 1 for cell in tower[i]) or all(cell == 0 for cell in tower[i]):
            # If the row is completely filled or empty, continue to the next row
            continue
        else:
            # If the row has a mix of filled and empty cells, return the current row
            return i + 1  # Rows are 1-indexed in the problem statement

# Example usage:
tower = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    # Next 9 rows are figured out as mentioned
]

result = find_first_sensible_row(tower)
print(result)

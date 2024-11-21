def get_overflow_list(grid):
    overflow_list = []
    # Get the number of rows and columns
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows): # Iterate through the rows
        for c in range(cols): # Iterate through the columns
            # Determine the number of neighbors for the current cell
            if (r == 0 and c == 0) or (r == 0 and c == cols - 1) or (r == rows - 1 and c == 0) or (r == rows - 1 and c == cols - 1):
                # Corner cells
                neighbors = 2
            elif r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                # Edge cells (but not corners)
                neighbors = 3
            else:
                # Non-edge cells
                neighbors = 4

            # Check if the cell will overflow
            if abs(grid[r][c]) >= neighbors:
                overflow_list.append((r, c))

    return overflow_list if overflow_list else None

def overflow(grid, a_queue):
    def all_same_sign(grid):
        # Create a list of non-zero cells to be checked
        non_zero_cells = [grid[r][c] for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] != 0]
        # Check if all elements are either positive or negative
        return all(n > 0 for n in non_zero_cells) or all(n < 0 for n in non_zero_cells)

    # Check for overflowing cells in the grid
    overflow_cells = get_overflow_list(grid)

    # Base case: if no cells are overflowing or all non-zero cells have the same sign
    if not overflow_cells or all_same_sign(grid):
        return 0  # No more grids will be added

    # Recursive case: Process overflowing cells

    # Update the overflowing cells to 0 and determine the sign
    for r, c in overflow_cells:
        sign = 1 if grid[r][c] > 0 else -1 # Determine the sign of the overflowing cell
        grid[r][c] = 0  # Set the overflowing cell to 0

    # Update neighbors for the current overflowing cell
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Right, Down, Left, Up
    for r, c in overflow_cells: # Iterate through the overflowing cells
        for n_r, n_c in neighbors:  # Iterate through the neighbors
            neighbor_r, neighbor_c = r + n_r, c + n_c # Calculate the new row and column
            if 0 <= neighbor_r < len(grid) and 0 <= neighbor_c < len(grid[0]): # Check if the neighbor is within the grid
                grid[neighbor_r][neighbor_c] = abs(grid[neighbor_r][neighbor_c]) + 1  # Increment the neighbor by 1
                grid[neighbor_r][neighbor_c] *= sign  # Apply the sign of the overflowing cell

    # Enqueue the new grid
    a_queue.enqueue([row[:] for row in grid])  # Enqueue a copy of the grid

    # Recursively call overflow on the new grid and add 1 to the count
    return overflow(grid, a_queue) + 1
def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None

def is_valid_move(grid, row, col, num):
    return (
        all(num != grid[row][c] for c in range(9)) and
        all(num != grid[r][col] for r in range(9)) and
        all(num != grid[r][c] for r in range(row - row % 3, row - row % 3 + 3) for c in range(col - col % 3, col - col % 3 + 3))
    )

def solve_sudoku(grid):
    row, col = find_empty_location(grid)
    if row is None:
        return True
    
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    
    return False

def main():
    # Example Sudoku grid
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(grid):
        print("Sudoku puzzle solved:")
        print_grid(grid)
    else:
        print("No solution exists for the Sudoku puzzle.")

if __name__ == "__main__":
    main()

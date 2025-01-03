from collections import defaultdict

class GuardPatrol:
    def __init__(self, file_path):
        # Read map, start position and initial direction
        self.grid, self.start_pos, self.start_dir = self.read_input(file_path)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.directions = {
            '^': (-1, 0),  # Up
            'v': (1, 0),   # Down 
            '<': (0, -1),  # Left
            '>': (0, 1)    # Right
        }
        self.turn_right = {
            '^': '>',
            '>': 'v',
            'v': '<',
            '<': '^'
        }

    def read_input(self, file_path):
        # Read map and starting position/direction from text file
        grid = []
        start_pos = None
        start_dir = None

        with open(file_path, 'r') as file:
            for y, line in enumerate(file):
                row = list(line.strip())
                for x, char in enumerate(row):
                    if char in '^>v<':
                        start_pos = (y, x)
                        start_dir = char
                grid.append(row)
        return grid, start_pos, start_dir

    def is_outside_grid(self, r, c):
        # Check if position is outside map boundaries
        return r < 0 or r >= self.rows or c < 0 or c >= self.cols

    def simulate_patrol(self, grid, r, c, direction):
        # Simulate guard movement with given map
        visited_states = set()
        while True:
            # Check current state
            state = (r, c, direction)
            if state in visited_states:
                return True  # Guard is in a loop
            visited_states.add(state)

            # Calculate next position
            dr, dc = self.directions[direction]
            next_r, next_c = r + dr, c + dc

            if self.is_outside_grid(next_r, next_c):
                return False  # Guard left the map

            if grid[next_r][next_c] == '#':
                direction = self.turn_right[direction]  # Turn right
            else:
                r, c = next_r, next_c  # Move forward

    def find_loop_positions(self):
        # Find all positions that would cause a loop if obstacle placed
        r, c = self.start_pos
        direction = self.start_dir
        loop_positions = set()

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == '.' and (row, col) != (r, c):
                    # Create new map with obstacle
                    new_grid = [list(row) for row in self.grid]
                    new_grid[row][col] = '#'

                    # Check for loop
                    if self.simulate_patrol(new_grid, r, c, direction):
                        loop_positions.add((row, col))

        return len(loop_positions)


if __name__ == "__main__":
    # Text file containing the map
    file_path = "input.txt"

    patrol = GuardPatrol(file_path)
    result = patrol.find_loop_positions()
    print(f"Number of possible positions for obstruction: {result}")

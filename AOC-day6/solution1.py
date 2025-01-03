# Class to solve guard patrol path problem
class Solution:
    def read_input(self):
        # Initialize empty grid and starting position/direction
        grid = []
        start_pos = None
        start_dir = None

        # Read input file line by line
        with open('input.txt', 'r') as file:
            for y, line in enumerate(file):
                row = list(line.strip())
                for x, char in enumerate(row):
                    # Find starting position and direction
                    if char in '^>v<':
                        start_pos = (y, x)
                        start_dir = char
                grid.append(row)
        return grid, start_pos, start_dir
    
    def get_next_direction(self, current_dir):
        # Map current direction to next direction when turning right
        directions = {
            '^': '>',
            '>': 'v',
            'v': '<',
            '<': '^'
        }
        return directions[current_dir]
    
    def get_next_position(self, pos, direction):
        # Map directions to coordinate changes
        moves = {
            '^': (-1, 0),  # Up
            '>': (0, 1),   # Right
            'v': (1, 0),   # Down
            '<': (0, -1)   # Left
        }
        dx, dy = moves[direction]
        return (pos[0] + dx, pos[1] + dy)    
    
    def is_valid_position(self, pos, grid):
        # Check if position is within grid boundaries
        rows = len(grid)
        cols = len(grid[0])
        return 0 <= pos[0] < rows and 0 <= pos[1] < cols
    
    def solve(self):
        # Get initial state from input
        grid, current_pos, current_dir = self.read_input()

        # Track visited positions
        visited = {current_pos}

        # Simulate guard movement
        while True:
            next_pos = self.get_next_position(current_pos, current_dir)

            # Stop if guard leaves grid
            if not self.is_valid_position(next_pos, grid):
                break

            # Turn right if wall encountered, otherwise move forward
            if grid[next_pos[0]][next_pos[1]] == '#':
                current_dir = self.get_next_direction(current_dir)
            else:
                current_pos = next_pos
                visited.add(current_pos)

        return len(visited)

if __name__ == '__main__':
    # Create solution instance and run
    solution = Solution()
    result = solution.solve()
    print(f"The guard visited {result} distinct positions.")


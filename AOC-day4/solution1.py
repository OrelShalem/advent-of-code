# Class to solve the XMAS grid search problem
class Solution:
    # Read input grid from file
    def read_input(self):
        # Open input file and convert each line into a list of characters
        with open('input.txt', 'r') as file:
            grid = [list(line.strip()) for line in file]
            return grid

    # Count occurrences of word in grid in all 8 directions
    def count_xmas_in_grid(self, grid:list, word:str = 'XMAS'):

        count = 0 # count of XMAS occurrences
        rows = len(grid) # number of rows in grid
        cols = len(grid[0]) # number of columns in grid 
        word_len = len(word) # length of word to search for

        # List of 8 possible directions to check:
        directions = [
            (0, 1), # right
            (0, -1), # left
            (1, 0), # down
            (-1, 0), # up
            (1, 1), # down-right
            (1, -1), # down-left
            (-1, 1), # up-right
            (-1, -1), # up-left
        ]

        # Check if word exists starting at (x,y) in direction (dx,dy)
        def is_valid(x, y, dx, dy):
            # Check each character of the word
            for i in range(word_len):
                nx, ny = x + i*dx, y + i*dy # Get next position
                # Return false if out of bounds or character doesn't match
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != word[i]:
                    return False
            return True

        # Check every starting position and direction
        for x in range(rows):
            for y in range(cols):
                for dx, dy in directions:
                    if is_valid(x, y, dx, dy):
                        count += 1
        return count


# Main execution
if __name__ == '__main__':
    # Create solution instance and run
    sol = Solution()
    grid = sol.read_input()
    print(sol.count_xmas_in_grid(grid))


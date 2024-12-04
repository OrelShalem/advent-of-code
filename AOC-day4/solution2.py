class Solution:
    def read_input(self):
        # Read input file and convert each line into a list of characters
        with open('input.txt', 'r') as file:
            grid = [list(line.strip()) for line in file]
            return grid
        
    def count_x_mas(self, grid: list):
        # Get dimensions of grid
        rows = len(grid)
        cols = len(grid[0])
        # Initialize counter for X-MAS patterns
        count = 0
        
        def check_mas(m, a, s):
            # Check if three points form either MAS or SAM pattern
            # m, a, s are tuples containing coordinates (row,col) for each letter
            return ((grid[m[0]][m[1]] == 'M' and grid[a[0]][a[1]] == 'A' and grid[s[0]][s[1]] == 'S') or
                   (grid[m[0]][m[1]] == 'S' and grid[a[0]][a[1]] == 'A' and grid[s[0]][s[1]] == 'M'))
        
        def is_x_mas(x, y):
            # Check if point (x,y) is center of an X-MAS pattern
            # Return False if point is too close to edges
            if x <= 0 or x >= rows - 1 or y <= 0 or y >= cols - 1:
                return False
                
            # Check all possible combinations of X pattern
            # Each leg of the X can be either MAS or SAM
            # The center point (x,y) must be 'A' with MAS/SAM patterns in both diagonals
            
            # Check if diagonals form valid MAS/SAM patterns:
            # Top-left to bottom-right + Top-right to bottom-left
            if (check_mas((x-1, y-1), (x, y), (x+1, y+1)) and 
                check_mas((x-1, y+1), (x, y), (x+1, y-1))):
                return True
                
            return False
        
        # Iterate through all points that could be centers of X patterns
        # Skip edge points since they can't form complete X patterns
        for x in range(1, rows - 1):
            for y in range(1, cols - 1):
                if is_x_mas(x, y):
                    count += 1
                    
        return count

if __name__ == '__main__':
    # Create solution instance and run
    sol = Solution()
    grid = sol.read_input()
    print(sol.count_x_mas(grid))
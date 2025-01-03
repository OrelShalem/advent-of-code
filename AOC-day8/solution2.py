class Solution:
    def parse_input(self):
        # Reads the map from file and returns list of rows
        grid = []
        with open('input.txt', 'r') as file:
            for line in file:
                grid.append(line.strip())
        return grid

    def find_antennas(self, grid):
        # Finds all antennas on the map by frequency
        antennas = {}
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell.isalnum():  # If cell contains frequency (letter or number)
                    if cell not in antennas:
                        antennas[cell] = []
                    antennas[cell].append((r, c))
        return antennas

    def calculate_antinode_positions(self, grid, antennas):
        # Calculates all antinode positions
        antinodes = set()
        rows = len(grid)
        cols = len(grid[0])

        for freq, positions in antennas.items():  # For each frequency
            if len(positions) < 2:
                continue
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    ant1 = positions[i]
                    ant2 = positions[j]
                    
                    antinodes.add(ant1)
                    antinodes.add(ant2)

                    # Check if the two antennas are collinear
                    for k in range(cols):
                        for l in range(rows):
                            point = (k, l)
                            if point != ant1 and point != ant2 :
                                if self.is_collinear(ant1, ant2, point):
                                    antinodes.add(point)

        return antinodes
    
    def is_collinear(self, p1, p2, p3):
        "checks if three points are collinear"
        return (p2[1] - p1[1]) * (p3[0] - p1[0]) == (p3[1] - p1[1]) * (p2[0] - p1[0])
    
    def count_total_antinodes(self, file_path):
        # Calculates the number of unique antinode locations
        grid = self.parse_input()
        antennas = self.find_antennas(grid)
        antinodes = self.calculate_antinode_positions(grid, antennas)
        return len(antinodes)


if __name__ == "__main__":
    solution = Solution()
    total_antinodes = solution.count_total_antinodes("input.txt")
    print(f"Total unique antinode locations: {total_antinodes}")

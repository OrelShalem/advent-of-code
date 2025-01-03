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

        for freq, positions in antennas.items():  # For each frequency
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    r1, c1 = positions[i]
                    r2, c2 = positions[j]

                    # Calculate midpoint
                    if (r1 + r2) % 2 == 0 and (c1 + c2) % 2 == 0:
                        mid_r, mid_c = (r1 + r2) // 2, (c1 + c2) // 2
                        antinodes.add((mid_r, mid_c))  # Midpoint is an antinode

                    # Calculate far and near points
                    dr, dc = r2 - r1, c2 - c1
                    far_r, far_c = r2 + dr, c2 + dc
                    near_r, near_c = r1 - dr, c1 - dc

                    # Check far point
                    if 0 <= far_r < len(grid) and 0 <= far_c < len(grid[0]):
                        antinodes.add((far_r, far_c))

                    # Check near point
                    if 0 <= near_r < len(grid) and 0 <= near_c < len(grid[0]):
                        antinodes.add((near_r, near_c))

        return antinodes

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

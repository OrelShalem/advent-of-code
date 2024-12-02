class Solution:
    
    # Check if the report (the values in the list) is safe
    # A report is considered safe if:
    # 1. The numbers are either strictly increasing or strictly decreasing
    # 2. The difference between adjacent numbers is between 1 and 3 inclusive
    def if_report_safe(self, report):
        # Check if numbers are strictly increasing
        increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
        # Check if numbers are strictly decreasing
        decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))
        # Check if difference between adjacent numbers is between 1-3
        valid_adjacent = all( 1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report)-1))
        # Return True if report is either increasing or decreasing AND has valid adjacent differences
        return (increasing or decreasing) and valid_adjacent
    
    # Count how many reports in the data are safe
    def count_report_safe(self, data):
        return sum(1 for report in data if self.if_report_safe(report))
    
    # Read input file and parse into list of integer lists
    def read_file(self, input_file):
        # Initialize empty list to store data
        data = []
        # Read file line by line
        with open(input_file, "r") as file:
            for line in file:
                # Convert each line to list of integers
                data.append([int(i) for i in line.strip().split()])
        return data

if __name__ == "__main__":
    # Test data with various cases
    data = [
    [7, 6, 4, 2, 1],  # Strictly decreasing
    [1, 2, 7, 8, 9],  # Strictly increasing
    [9, 7, 6, 2, 1],  # Strictly decreasing
    [1, 3, 2, 4, 5],  # Not monotonic
    [8, 6, 4, 4, 1],  # Not strictly decreasing
    [1, 3, 6, 7, 9]   # Strictly increasing
    ]
    # Create solution instance
    solution = Solution()
    # Test with example data
    print(solution.count_report_safe(data))
    # Test with actual input file
    data = solution.read_file("input2.txt")
    print(solution.count_report_safe(data))


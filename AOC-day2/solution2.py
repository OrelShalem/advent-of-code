class Solution:

    def check_basic_safe(self, report):
        # Check if the report is strictly increasing
        increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
        # Check if the report is strictly decreasing 
        decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))
        # Check if the difference between adjacent numbers is between 1 and 3 inclusive
        valid_adjacent = all( 1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report)-1))
        # Report is basic safe if it's either increasing or decreasing AND has valid adjacent differences
        return (increasing or decreasing) and valid_adjacent
    
    def if_report_safe(self, report):
        # First check if report meets basic safety criteria
        if self.check_basic_safe(report):
            return True
        # If not basic safe, check if it can be made safe by removing elements
        return self.if_report_safe_2(report)

    def if_report_safe_2(self, report):
        # Try removing each element one at a time
        for i in range(len(report)):
            # Create new report without element at index i
            modified_report = report[:i] + report[i+1:]
            # Check if modified report is basic safe
            if self.check_basic_safe(modified_report):
                return True
        return False
    
    def count_report_safe(self, data):
        # Count how many reports in the data are safe
        return sum(1 for report in data if self.if_report_safe(report))
    
    def read_file(self, input_file):
        # Initialize empty list to store data
        data = []
        # Read input file line by line
        with open(input_file, "r") as file:
            for line in file:
                # Convert each line to list of integers
                data.append([int(i) for i in line.strip().split()])
        return data

if __name__ == "__main__":
    # Test data
    data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
    ]
    # Create solution instance
    solution = Solution()
    # Test with example data
    print(solution.count_report_safe(data))
    # Read and test with actual input file
    data = solution.read_file("input2.txt")
    print(solution.count_report_safe(data))


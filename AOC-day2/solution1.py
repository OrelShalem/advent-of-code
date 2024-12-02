class Solution:
    
    # check if the report (the values in the dict) is safe
    def if_report_safe(self, report):
        increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
        decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))

        valid_adjacent = all( 1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report)-1))
        return (increasing or decreasing) and valid_adjacent
    
    def count_report_safe(self, data):
        return sum(1 for report in data if self.if_report_safe(report))
    
    def read_file(self, input_file):
        data = []
        with open(input_file, "r") as file:
            for line in file:
                data.append([int(i) for i in line.strip().split()])
        return data

if __name__ == "__main__":
    #test
    data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
    ]
    solution = Solution()
    print(solution.count_report_safe(data))
    data = solution.read_file("input2.txt")
    print(solution.count_report_safe(data))


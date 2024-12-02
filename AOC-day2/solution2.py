class Solution:

    def check_basic_safe(self, report):
        increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
        decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))
        valid_adjacent = all( 1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report)-1))
        return (increasing or decreasing) and valid_adjacent
    
    # check if the report (the values in the dict) is safe
    def if_report_safe(self, report):
        if self.check_basic_safe(report):
            return True
        return self.if_report_safe_2(report)
    # after we checked the report is safe, we need to check if the report will be safe if we remove the any number of elements from the report
    def if_report_safe_2(self, report):
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if self.check_basic_safe(modified_report):
                return True
        return False
    
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


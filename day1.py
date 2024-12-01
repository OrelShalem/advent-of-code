# Class to handle list operations and calculations
class Solution:
    def __init__(self):
        # Initialize empty lists to store left and right values
        self.left_list = []
        self.right_list = []

    def claculate_total_distance(self, list1, list2):
        # Calculate absolute difference between corresponding elements
        total_distance = 0
        for i in range(len(list1)):
            total_distance += abs(list1[i] - list2[i])
        return total_distance
    
    def sort_list_low_to_high(self, list):
        # Sort list in ascending order
        return sorted(list)

    def read_input_file(self, file_path):
        # Read input file and parse into two lists
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line into left and right values
                left, right = map(int, line.split())
                self.left_list.append(left)
                self.right_list.append(right)
        return self.left_list, self.right_list

# Main execution
if __name__ == "__main__":
    # Input file path
    file_path = "input.txt"
    
    # Create solution instance
    solution = Solution()
    
    # Read and parse input file
    left_list, right_list = solution.read_input_file(file_path)
    
    # Sort both lists
    left_list = solution.sort_list_low_to_high(left_list)
    right_list = solution.sort_list_low_to_high(right_list)
    
    # Calculate total distance between sorted lists
    total_distance = solution.claculate_total_distance(left_list, right_list)
    
    # Print result
    print(total_distance)
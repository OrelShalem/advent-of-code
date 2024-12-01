# Class to handle list operations and similarity score calculations
class Solution:
    def __init__(self):
        # Initialize empty lists to store left and right values
        self.left_list = []
        self.right_list = []


    def read_input_file(self, file_path):
        # Read input file and parse into two lists
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line into left and right values
                left, right = map(int, line.split())
                self.left_list.append(left)
                self.right_list.append(right)
        return self.left_list, self.right_list
    
    def calculate_similarity_score(self, left_list, right_list):
        # Initialize similarity score
        similarity_score = 0
        # Dictionary to store frequency count of numbers in right_list
        diractory = {}
        # Count frequency of each number in right_list
        for i in range(len(right_list)):
            if right_list[i] in diractory:
                diractory[right_list[i]] += 1
            else:
                diractory[right_list[i]] = 1
        # Calculate similarity score by multiplying number with its frequency if present in both lists
        for i in range(len(left_list)):
            if left_list[i] in diractory:
                similarity_score += (diractory[left_list[i]] * left_list[i])
        return similarity_score
    
# Main execution block
if __name__ == "__main__":
    # Create solution instance
    solution = Solution()
    # Test case with sample input
    left_list = [3,4,2,1,3,3]
    right_list = [4,3,5,3,9,3]
    print(solution.calculate_similarity_score(left_list, right_list))
    # Process actual input file
    left_list, right_list = solution.read_input_file("input.txt")
    print(solution.calculate_similarity_score(left_list, right_list))

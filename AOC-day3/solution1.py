# Import regex module for pattern matching
import re


class Solution:
    def read_from_file(self, file_path: str) -> str:
        # Open and read contents of file
        with open(file_path, 'r') as file:
            return file.read()
        
    def extract_mul_instructions(self, input: str) -> list:
        # Pattern to match mul(x,y) instructions
        pattern = r"mul\((\d+),(\d+)\)"
        # Find all matching patterns in input
        return re.findall(pattern, input)
    
    def calculate_sum_of_multiplications(self, instructions: list) -> int:
        # Calculate sum of all multiplications from instructions
        return sum(int(a) * int(b) for a, b in instructions)
    
    def run(self):
        # Read input from file
        input = self.read_from_file("input.txt")
        # Extract multiplication instructions
        instructions = self.extract_mul_instructions(input)
        # Calculate total sum of multiplications
        sum_of_multiplications = self.calculate_sum_of_multiplications(instructions)
        # Print result
        print(sum_of_multiplications)

    # Program entry point
if __name__ == "__main__":
    solution = Solution()
    solution.run()



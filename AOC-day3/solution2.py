# Import regex module for pattern matching
import re

class Solution:
    def read_from_file(self, file_path: str) -> str:
        with open(file_path, 'r') as file:
            return file.read()
        
    def extract_mul_instructions(self, input: str) -> int:
        # Pattern to match mul(x,y), do() and don't() instructions
        pattern = r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)'
        enabled = True  # Flag to track if multiplications are enabled
        total_multiplications = 0

        # Find all matching instructions in the input
        matches = re.finditer(pattern, input)

        for match in matches:
            match_str = match.group()
            
            if match_str == "do()":
                enabled = True  # Enable multiplications
            elif match_str == "don't()":
                enabled = False  # Disable multiplications
            else:  # Must be a mul(x,y) instruction
                if enabled:
                    # Extract the two numbers from mul(x,y)
                    nums = re.findall(r'\d+', match_str)
                    x, y = int(nums[0]), int(nums[1])
                    total_multiplications += x * y

        return total_multiplications

    def run(self):
        input = self.read_from_file("input.txt")
        result = self.extract_mul_instructions(input)
        print(result)

# Program entry point
if __name__ == "__main__":
    solution = Solution()
    solution.run()


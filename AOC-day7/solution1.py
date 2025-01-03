from itertools import product # for generating all possible combinations of numbers and operators

class Solution:
    def parse_input(self):
        # Initialize empty list to store equations
        equations = []

        # Open and read input file
        with open('input.txt', 'r') as file:
            for line in file:
                target, numbers = line.split(':')
                target = int(target.strip()) # target is the number of the register
                numbers = list(map(int, numbers.strip().split())) # numbers are the numbers to be used in the equation
                equations.append((target, numbers))
        return equations
    
    def evaluate_expression(self, numbers, operators):
        result = numbers[0] # start with the first number
        for i, op in enumerate(operators): # iterate over the operators
            if op == '+':
                result += numbers[i + 1] # add next number
            elif op == '*':
                result *= numbers[i + 1] # multiply by next number
        return result
        
    def is_equation_valid(self, target, numbers):
        # Calculate number of operators needed
        n = len(numbers) - 1 # number of operators needed is one less than number of numbers

        # Try all possible combinations of operators
        for ops in product('+*', repeat=n):
            if self.evaluate_expression(numbers, ops) == target:
                return True # Found valid combination
        return False # No valid combination found

    def calculate_total_calibration(self, equations):
        # Initialize sum
        total = 0
        # Check each equation
        for target, numbers in equations:
            if self.is_equation_valid(target, numbers):
                total += target # Add target value if equation is valid
        return total


if __name__ == "__main__":
    solution = Solution() # Create solution instance
    equations = solution.parse_input() # Parse input file
    total_calibration = solution.calculate_total_calibration(equations) # Calculate total
    print(total_calibration) # Print result


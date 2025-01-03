# Class for solving equations with different operators
class Solution:
    def parse_input(self):
        # Read input file and return list of equations
        equations = []
        with open('input.txt', 'r') as file:
            for line in file:
                target, numbers = line.split(':')
                target = int(target.strip()) # Convert target to integer
                numbers = list(map(int, numbers.strip().split())) # Convert numbers to list of integers
                equations.append((target, numbers))
        return equations

    def is_equation_valid_recursive(self, numbers, target, current_index, current_value):
        # Recursively check if target can be reached using operators
        if current_index == len(numbers):  # If we reached end of list
            return current_value == target

        next_number = numbers[current_index]

        # Try all possible operators
        # Addition
        if self.is_equation_valid_recursive(numbers, target, current_index + 1, current_value + next_number):
            return True
        # Multiplication 
        if self.is_equation_valid_recursive(numbers, target, current_index + 1, current_value * next_number):
            return True
        # Concatenation
        concatenated_value = int(str(current_value) + str(next_number))
        if self.is_equation_valid_recursive(numbers, target, current_index + 1, concatenated_value):
            return True

        return False  # If no operator worked

    def is_equation_valid(self, target, numbers):
        # Check if equation is valid using recursive function
        # Start with first number
        return self.is_equation_valid_recursive(numbers, target, 1, numbers[0])

    def calculate_total_calibration(self, equations):
        # Calculate sum of target values for valid equations
        total = 0
        for target, numbers in equations:
            if self.is_equation_valid(target, numbers):
                total += target
        return total


if __name__ == "__main__":
    solution = Solution() # Create solution instance
    equations = solution.parse_input() # Parse input file
    total_calibration = solution.calculate_total_calibration(equations) # Calculate total
    print(total_calibration) # Print result

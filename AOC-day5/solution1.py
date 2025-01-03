# Import defaultdict for graph representation
from collections import defaultdict

# Class to solve the page update ordering problem
class Solution:
    # Read and parse input file containing rules and updates
    def read_input(self):
        # Initialize empty lists to store rules and updates
        rules = []
        updates = []
        # Flag to track whether we're reading rules or updates section
        reading_rules = True

        # Open and read input file
        with open('input.txt', 'r') as file:
            for line in file:
                # Remove whitespace from line
                line = line.strip()
                # Empty line separates rules from updates
                if not line: # empty line means end of rules
                    reading_rules = False
                    continue
                
                if reading_rules:
                    # Parse rule line - split on | character
                    x, y = line.split('|')
                    # Convert to integers and add to rules list
                    rules.append((int(x), int(y)))
                else:
                    # Parse update line - split on comma and convert to integers
                    update = [int(x) for x in line.split(',')]
                    # Add update list to updates
                    updates.append(update)
        
        # Return parsed rules and updates
        return rules, updates

    # Build directed graph from dependency rules
    def build_graph(self, rules):
        graph = defaultdict(list)
        for x, y in rules:
            graph[x].append(y)
        return graph

    # Check if update order satisfies all dependencies
    def is_valid_order(self, update, graph):
        # Convert update list to set for O(1) lookups
        update_set = set(update)

        # Check each page in the update order
        for i, current in enumerate(update):
            # Check all pages that depend on current page
            for dependent in graph[current]:
                # If dependent page is in update list
                if dependent in update_set:
                    # Get position of dependent page
                    j = update.index(dependent)
                    # Invalid if dependent comes before current
                    if j < i:
                        return False
        return True

    # Get middle page number from update list
    def get_middle_page(self, update):
        return update[len(update) // 2]

    # Calculate sum of middle pages from valid updates
    def calculate_middle_sum(self):
        # Get input data
        rules, updates = self.read_input()
        # Build dependency graph
        graph = self.build_graph(rules)

        middle_sum = 0
        # Process each update
        for update in updates:
            if self.is_valid_order(update, graph):
                middle_sum += self.get_middle_page(update)
        return middle_sum


# Run solution if file is executed directly
if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate_middle_sum())


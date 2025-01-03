# Import defaultdict for graph representation
from collections import defaultdict

class Solution:
    # Read and parse input file containing rules and updates
    def read_input(self):
        rules = []
        updates = []
        reading_rules = True

        with open('input.txt', 'r') as file:
            for line in file:
                line = line.strip()
                # Empty line separates rules from updates
                if not line:
                    reading_rules = False
                    continue
                
                if reading_rules:
                    # Parse rule line - split on | character
                    x, y = line.split('|')
                    rules.append((int(x), int(y)))
                else:
                    # Parse update line - split on comma and convert to integers
                    update = [int(x) for x in line.split(',')]
                    updates.append(update)
        
        return rules, updates

    # Build directed graph from dependency rules
    def build_graph(self, rules):
        graph = defaultdict(list)
        for x, y in rules:
            graph[x].append(y)
        return graph

    # Check if update order satisfies all dependencies
    def is_valid_order(self, update, graph):
        update_set = set(update)
        for i, current in enumerate(update):
            for dependent in graph[current]:
                if dependent in update_set:
                    j = update.index(dependent)
                    if j < i:
                        return False
        return True

    # Get middle page number from update list
    def get_middle_page(self, update):
        return update[len(update) // 2]

    # Build graph with in-degree counts for relevant pages
    def build_graph_with_indegrees(self, rules, pages):
        graph = defaultdict(list)
        indegrees = {page: 0 for page in pages}
        
        # Only add edges between pages in the current update
        for x, y in rules:
            if x in pages and y in pages:
                graph[x].append(y)
                indegrees[y] += 1
        return graph, indegrees

    # Sort pages in topological order
    def topological_sort(self, update, rules):
        pages = set(update)
        graph, indegrees = self.build_graph_with_indegrees(rules, pages)
        
        # Initialize queue with pages having no dependencies
        queue = []
        for page in pages:
            if indegrees[page] == 0:
                queue.append(page)
        
        result = []
        remaining_pages = set(pages)
        
        while queue:
            # Take page with highest number among available pages
            current = max(queue)
            queue.remove(current)
            result.append(current)
            remaining_pages.remove(current)
            
            # Update in-degrees of dependent pages
            for neighbor in graph[current]:
                if neighbor in remaining_pages:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        queue.append(neighbor)
        
        return result

    # Calculate sum of middle pages for invalid updates after sorting
    def calculate_middle_sum_part2(self):
        rules, updates = self.read_input()
        graph = self.build_graph(rules)
        
        middle_sum = 0
        for update in updates:
            # Only process invalid updates
            if not self.is_valid_order(update, graph):
                sorted_update = self.topological_sort(update, rules)
                middle_sum += self.get_middle_page(sorted_update)
        
        return middle_sum

# Run solution if file is executed directly
if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate_middle_sum_part2())
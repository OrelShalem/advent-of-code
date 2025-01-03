class DiskFragmenter:
    def __init__(self, disk_map):
        self.disk_map = disk_map
        self.blocks = self.parse_disk_map()

    def parse_disk_map(self):
        """Converts the disk map into an array of blocks"""
        blocks = []
        file_id = 0
        is_file = True

        for length in map(int, self.disk_map):
            if is_file:
                blocks.extend([file_id] * length)
                file_id += 1
            else:
                blocks.extend(['.'] * length)
            is_file = not is_file

        return blocks

    def find_files(self):
        """Finds all files in the system and returns their info"""
        files = {}  # {id: (start_pos, length)}
        current_file = None
        start_pos = None
        length = 0

        for i, block in enumerate(self.blocks):
            if isinstance(block, int):  # If it's a file block
                if block != current_file:  # New file
                    if current_file is not None:
                        files[current_file] = (start_pos, length)
                    current_file = block
                    start_pos = i
                    length = 1
                else:  # Continuation of same file
                    length += 1

        # Handle last file
        if current_file is not None:
            files[current_file] = (start_pos, length)

        return files

    def find_free_space(self, needed_length, file_start_pos):
        """Finds the first free space to the left that fits the file"""
        current_length = 0
        start_pos = None
        
        # Important: only check positions before current file location
        for i in range(file_start_pos):
            if self.blocks[i] == '.':
                if current_length == 0:  # Start of new sequence
                    start_pos = i
                current_length += 1
                # If we found enough space, return immediately
                if current_length >= needed_length:
                    return start_pos
            else:  # Hit an occupied block
                current_length = 0
                start_pos = None
        
        # If no suitable space found
        return None

    def move_file(self, file_id, from_pos, length, to_pos):
        """Moves an entire file to a new location"""
        # Copy file to new location
        for i in range(length):
            self.blocks[to_pos + i] = file_id
        # Delete file from old location
        for i in range(length):
            self.blocks[from_pos + i] = '.'

    def compact_files(self):
        """Compacts files according to part 2 rules"""
        files = self.find_files()
        
        # Process files in descending order of ID
        for file_id in sorted(files.keys(), reverse=True):
            start_pos, length = files[file_id]
            
            # Look for suitable space to the left
            new_pos = self.find_free_space(length, start_pos)
            
            # Move file only if free space found
            if new_pos is not None:
                self.move_file(file_id, start_pos, length, new_pos)

    def calculate_checksum(self):
        """Calculates the final checksum"""
        checksum = 0
        for pos, block in enumerate(self.blocks):
            if isinstance(block, int):  # If it's a file
                checksum += pos * block
        return checksum

def solve_part2(input_data):
    """Solves part 2 of the challenge"""
    fragmenter = DiskFragmenter(input_data)
    fragmenter.compact_files()
    return fragmenter.calculate_checksum()

if __name__ == "__main__":
    # Read input from file
    with open('input.txt', 'r') as file:
        file_input = file.read().strip()
    
    # Run solution and print result
    result = solve_part2(file_input)
    print(f"Part 2 Checksum: {result}")
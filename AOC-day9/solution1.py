class DiskFragmenter:
    def __init__(self, disk_map):
        self.disk_map = disk_map
        self.blocks = self.build_blocks()

    def build_blocks(self):
        """Converts the disk map into an array of blocks"""
        blocks = []
        file_id = 0
        is_file = True  # Start with a file

        for length in map(int, self.disk_map):
            if is_file:
                # Add blocks for file with file_id
                blocks.extend([file_id] * length)
                file_id += 1
            else:
                # Add empty blocks
                blocks.extend(['.'] * length)
            is_file = not is_file

        return blocks

    def compact_files(self):
        """Moves all files from end to start efficiently"""
        n = len(self.blocks)
        last_empty = None
        
        # Find first empty position
        for i in range(n):
            if self.blocks[i] == '.':
                last_empty = i
                break
        
        # If no empty space found, no need to compact
        if last_empty is None:
            return
        
        # Go through files from end to start
        for i in range(n-1, last_empty, -1):
            if self.blocks[i] != '.':  # If we found a file
                # Move file to empty space
                if last_empty < i:
                    self.blocks[last_empty] = self.blocks[i]
                    self.blocks[i] = '.'
                    # Update next empty position
                    last_empty += 1
                    # Find next empty position
                    while last_empty < i and self.blocks[last_empty] != '.':
                        last_empty += 1

    def calculate_checksum(self):
        """Calculates the filesystem checksum"""
        checksum = 0
        for pos, block in enumerate(self.blocks):
            if isinstance(block, int):  # If it's a file (not space)
                checksum += pos * block
        return checksum

def solve(input_data):
    fragmenter = DiskFragmenter(input_data)
    fragmenter.compact_files()
    return fragmenter.calculate_checksum()

if __name__ == "__main__":

    with open('input.txt', 'r') as file:
        file_input = file.read().strip()

    result = solve(file_input)
    print(f"Checksum: {result}")

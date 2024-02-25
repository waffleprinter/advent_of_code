def update_grid(instruction, start, end):
    for r in range(start[0], end[0] + 1):
        for c in range(start[1], end[1] + 1):
            if instruction == 'turn on':
                grid[r][c] = True
            
            elif instruction == 'turn off':
                grid[r][c] = False

            else:
                grid[r][c] = not grid[r][c]


grid = [[False for i in range(1000)] for i in range(1000)]

with open(r"Inputs\2015 Day 6 - Probably a Fire Hazard.txt", 'r') as f:
    for line in f.readlines():
        instruction = None

        if line.startswith("turn on"):
            instruction = "turn on"
            line = line[8:]

        elif line.startswith("turn off"):
            instruction = "turn off"
            line = line[9:]

        else:
            instruction = "toggle"
            line = line[7:]

        line = line.split()

        start = list(map(int, line[0].split(',')))
        end = list(map(int, line[2].split(',')))

        update_grid(instruction, start, end)

print(sum(sum(row) for row in grid))
        

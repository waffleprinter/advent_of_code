with open(r"Inputs\2015 Day 3 - Perfectly Spherical Houses in a Vacuum.txt", "r") as f:
    instructions = f.read()

x = y = 0
visited_houses = {(x, y)}

for char in instructions:
    if char == '^':
        y += 1

    elif char == '>':
        x += 1

    elif char == 'v':
        y -= 1

    elif char == '<':
        x -= 1

    visited_houses.add((x, y))

print(len(visited_houses))

def part1(instructions):
    x = y = 0
    visited_houses = set((x, y))

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

    return len(visited_houses)


def part2(instructions):
    santa_position = [0, 0]
    robo_santa_position = [0, 0]

    visited_houses = {(0, 0)}

    is_santas_turn_to_move = True

    for char in instructions:
        position_to_update = santa_position if is_santas_turn_to_move else robo_santa_position

        if char == '^':
            position_to_update[1] += 1

        elif char == '>':
            position_to_update[0] += 1

        elif char == 'v':
            position_to_update[1] -= 1

        elif char == '<':
            position_to_update[0] -= 1

        visited_houses.add(tuple(position_to_update))
        is_santas_turn_to_move = not is_santas_turn_to_move

    return len(visited_houses)
    

with open(r"C:\Users\jccpa\advent_of_code\2015 Day 3 - Perfectly Spherical Houses in a Vacuum.txt", "r") as f:
    instructions = f.read()

print(part1(instructions))
print(part2(instructions))
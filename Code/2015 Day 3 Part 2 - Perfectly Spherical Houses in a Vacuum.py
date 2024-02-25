with open(r"Inputs\2015 Day 3 - Perfectly Spherical Houses in a Vacuum.txt", "r") as f:
    instructions = f.read()

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

print(len(visited_houses))
def get_ribbon_square_footage(l, w, h):
    sorted_measurements = sorted([l, w, h])
    smallest_perimeter = 2 * sum(sorted_measurements[0:2])

    box_volume = l * w * h

    return smallest_perimeter + box_volume


with open(r"Inputs\2015 Day 2 - I Was Told There Would Be No Math.txt", "r") as f:
    box_dimensions = f.readlines()

total_ribbon_square_footage = 0
    
for dimensions in box_dimensions:
    dimensions = list(map(int, dimensions.split('x')))
    length, width, height, = dimensions[0], dimensions[1], dimensions[2]

    total_ribbon_square_footage += get_ribbon_square_footage(length, width, height)

print(total_ribbon_square_footage)
def calculate_box_area(l, w, h):
    side1 = l * w
    side2 = w * h
    side3 = h * l

    slack = min(side1, side2, side3)

    return 2 * (side1 + side2 + side3) + slack


def get_ribbon_square_footage(l, w, h):
    sorted_measurements = sorted([l, w, h])
    smallest_perimeter = 2 * sum(sorted_measurements[0:2])

    box_volume = l * w * h

    return smallest_perimeter + box_volume


with open(r"C:\Users\jccpa\advent_of_code\2015 Day 2 - I Was Told There Would Be No Math.txt", "r") as f:
    box_dimensions = f.readlines()

total_wrapping_paper_square_footage = 0
total_ribbon_square_footage = 0
    
for dimensions in box_dimensions:
    dimensions = dimensions.replace('\n', '')
    dimensions = dimensions.split('x')
    dimensions = list(map(int, dimensions))

    length = dimensions[0]
    width = dimensions[1]
    height = dimensions[2]

    total_wrapping_paper_square_footage += calculate_box_area(length, width, height)
    total_ribbon_square_footage += get_ribbon_square_footage(length, width, height)

print(total_wrapping_paper_square_footage)
print(total_ribbon_square_footage)
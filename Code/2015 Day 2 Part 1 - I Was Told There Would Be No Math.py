def calculate_box_area(l, w, h):
    side1 = l * w
    side2 = w * h
    side3 = h * l

    slack = min(side1, side2, side3)

    return 2 * (side1 + side2 + side3) + slack

with open(r"Inputs\2015 Day 2 - I Was Told There Would Be No Math.txt", "r") as f:
    box_dimensions = f.readlines()

total_wrapping_paper_square_footage = 0
    
for dimensions in box_dimensions:
    dimensions = list(map(int, dimensions.split('x')))
    length, width, height = dimensions[0], dimensions[1], dimensions[2]

    total_wrapping_paper_square_footage += calculate_box_area(length, width, height)

print(total_wrapping_paper_square_footage)

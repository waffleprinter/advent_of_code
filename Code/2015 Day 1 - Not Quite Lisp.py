def part1():
    ans = 0

    for char in parentheses:
        ans += 1 if char == '(' else -1

    return ans


def part2():
    ans = 0
    index = -1

    while ans != -1:
        index += 1
        ans += 1 if parentheses[index] == '(' else -1

    return index + 1


with open(r"C:\Users\jccpa\advent_of_code\2015 Day 1 - Not Quite Lisp.txt", "r") as f:
    parentheses = f.read()

print(part1())
print(part2())
def is_nice_string(string):
    contains_non_overlapping_double = False
    contains_separated_repeating_characters = False

    for i in range(len(string) - 2):
        for j in range(i + 2, len(string) - 1):
            if string[i:i + 2] == string[j: j + 2]:
                contains_non_overlapping_double = True

        if string[i] == string[i + 2]:
            contains_separated_repeating_characters = True

    return contains_non_overlapping_double and contains_separated_repeating_characters
            


vowels = {'a', 'e', 'i', 'o', 'u'}
forbidden_strings = {"ab", "cd", "pq", "xy"}

nice_strings = 0

with open(r"Inputs\2015 Day 5 - Doesn't He Have Intern Elves For This.txt", 'r') as f:
    for string in f.readlines():
        nice_strings += is_nice_string(string.replace("\n", ''))

print(nice_strings)

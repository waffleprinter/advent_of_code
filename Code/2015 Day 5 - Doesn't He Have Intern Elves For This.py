from timeit import default_timer


def is_nice_string_part_1(string):
    amount_of_vowels = 0
    contains_double_letter = False
    contains_forbidden_strings = False

    for i in range(len(string) - 1):
        amount_of_vowels += string[i] in vowels

        if string[i] == string[i + 1]:
            contains_double_letter = True

        if string[i: i + 2] in forbidden_strings:
            contains_forbidden_strings = True

    amount_of_vowels += string[-1] in vowels

    return amount_of_vowels >= 3 and contains_double_letter and not contains_forbidden_strings


def is_nice_string_part_2(string):
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

amount_of_nice_strings_part_1 = 0
amount_of_nice_strings_part_2 = 0

with open(r"C:\Users\jccpa\advent_of_code\Inputs\2015 Day 5 - Doesn't He Have Intern Elves For This.txt", 'r') as f:
    for string in f.readlines():
        string = string.replace('\n', '')

        amount_of_nice_strings_part_1 += is_nice_string_part_1(string)
        amount_of_nice_strings_part_2 += is_nice_string_part_2(string)


print(amount_of_nice_strings_part_1)
print(amount_of_nice_strings_part_2)

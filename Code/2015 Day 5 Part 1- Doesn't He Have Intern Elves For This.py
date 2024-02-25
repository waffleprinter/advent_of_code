def is_nice_string(string):
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


vowels = {'a', 'e', 'i', 'o', 'u'}
forbidden_strings = {"ab", "cd", "pq", "xy"}

nice_strings = 0

with open(r"Inputs\2015 Day 5 - Doesn't He Have Intern Elves For This.txt", 'r') as f:
    for string in f.readlines():
        nice_strings += is_nice_string(string.replace("\n", ''))

print(nice_strings)

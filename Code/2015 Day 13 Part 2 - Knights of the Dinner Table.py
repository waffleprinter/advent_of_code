from itertools import permutations


def calculate_happiness_score(sitting_arrangement):
    happiness_score = 0

    for i in range(len(sitting_arrangement) - 1):
        person1 = sitting_arrangement[i]
        person2 = sitting_arrangement[i + 1]

        happiness_score += happiness_dict[(person1, person2)]
        happiness_score += happiness_dict[(person2, person1)]

    happiness_score += happiness_dict[sitting_arrangement[0], sitting_arrangement[-1]]
    happiness_score += happiness_dict[sitting_arrangement[-1], sitting_arrangement[0]]

    return happiness_score


happiness_dict = {}

with open(r"Inputs\2015 Day 13 Part 1 - Knights of the Dinner Table.txt") as f:
    for statement in f.readlines():
        statement = statement.split()
        
        person1 = statement[0]
        person2 = statement[-1][:-1]

        happiness = int(statement[3]) if statement[2] == 'gain' else -int(statement[3])

        happiness_dict[(person1, person2)] = happiness

people = set(pair[0] for pair in happiness_dict)

for person in people:
    happiness_dict[("Me", person)] = 0
    happiness_dict[(person, "Me")] = 0

people.add("Me")

sitting_arrangements = permutations(people)

print(max(calculate_happiness_score(sitting_arrangement) for sitting_arrangement in sitting_arrangements))

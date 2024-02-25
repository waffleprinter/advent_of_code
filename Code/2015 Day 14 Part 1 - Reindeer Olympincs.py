def calculate_distance_traveled(speed, run_time, rest_time):
    distance_traveled = speed * run_time * int(race_length / (run_time + rest_time))
    
    if run_time < race_length % (run_time + rest_time):
        distance_traveled += speed * run_time

    else:
        distance_traveled += speed * (race_length % (run_time + rest_time))

    return distance_traveled


race_length = 2503
winning_distance = 0

with open(r"Inputs\2015 Day 14 - Reindeer Olympics.txt", 'r') as f:
    for stats in f.readlines():
        stats = stats.split()

        speed = int(stats[3])
        run_time = int(stats[6])
        rest_time = int(stats[13])

        distance_traveled = calculate_distance_traveled(speed, run_time, rest_time)

        if distance_traveled > winning_distance:
            winning_distance = distance_traveled

print(winning_distance)
        
import re

INPUT_FILE = '06-input.txt'

def compute_distance(race_max_time, pressure_time):
    return (race_max_time - pressure_time) * pressure_time

def get_number_of_ways_to_win(race_max_time, distance_min):
    sum = 0
    for pressure_time in range(1, race_max_time):
        if compute_distance(race_max_time, pressure_time) > distance_min:
            sum += 1
    return sum

def compute_part1(INPUT_FILE):
    part1 = 1
    with open(INPUT_FILE, 'r') as f:
        times_s,distances_s = f.readlines()
    distances = [part for part in distances_s[:-1].split(" ") if part][1:]
    times = [part for part in times_s[:-1].split(" ") if part][1:]
    print(distances)
    print(times)
    for i in range(len(times)):
        race_max_time = int(times[i])
        distance_min = int(distances[i])
        part1 *= get_number_of_ways_to_win(race_max_time, distance_min)
    return part1

def main():
    part1 = 1
    with open(INPUT_FILE, 'r') as f:
        times_s,distances_s = f.readlines()
    distances = [part for part in distances_s[:-1].split(" ") if part][1:]
    times = [part for part in times_s[:-1].split(" ") if part][1:]
    print(distances)
    print(times)
    for i in range(len(times)):
        race_max_time = int(times[i])
        distance_min = int(distances[i])
        part1 *= get_number_of_ways_to_win(race_max_time, distance_min)
    return part1

print(main())

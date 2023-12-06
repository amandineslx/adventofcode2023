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

def compute_part1():
    part1 = 1
    with open(INPUT_FILE, 'r') as f:
        times_s,distances_s = f.readlines()
    distances = [part for part in distances_s[:-1].split(" ") if part][1:]
    times = [part for part in times_s[:-1].split(" ") if part][1:]
    for i in range(len(times)):
        race_max_time = int(times[i])
        distance_min = int(distances[i])
        part1 *= get_number_of_ways_to_win(race_max_time, distance_min)
    return part1

def compute_part2():
    part2 = 0
    with open(INPUT_FILE, 'r') as f:
        time_s,distance_s = f.readlines()
    time = int(time_s.replace(" ", "").split(":")[1])
    distance = int(distance_s.replace(" ", "").split(":")[1])
    for i in range(1,time+1):
        if compute_distance(time, i) > distance:
            part2 += 1
    return part2

def main():
    return compute_part1(), compute_part2()

print(main())

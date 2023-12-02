import re

INPUT_FILE = '02-input.txt'
TARGETS = {
    "red": 12,
    "green": 13,
    "blue": 14
}
REGEX_GAME_NUMBER = '^Game (\d+):'
REGEX_COLOR = '(\d+) %s'

def get_max_color(line, color):
    max_color = 0
    regex = re.compile(REGEX_COLOR % color)
    for match in regex.finditer(line):
        integer_match = int(match.group(1))
        if integer_match > max_color:
            max_color = integer_match
    return max_color

def get_sum_for_game(line):
    for color in TARGETS.keys():
        max_color = get_max_color(line, color)
        if max_color > TARGETS[color]:
            return 0
    return int(re.search(REGEX_GAME_NUMBER, line).group(1))

def get_power_for_game(line):
    power = 1
    for color in TARGETS.keys():
        max_color = get_max_color(line, color)
        power = power * max_color
    return power

def main():
    sum_part_one,sum_part_two = 0,0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            sum_part_one = sum_part_one + get_sum_for_game(line)
            sum_part_two = sum_part_two + get_power_for_game(line)
    return sum_part_one,sum_part_two

print(main())

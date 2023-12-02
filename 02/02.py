import re

INPUT_FILE = '02-input.txt'
TARGETS = {
    "red": 12,
    "green": 13,
    "blue": 14
}
REGEX_GAME_NUMBER = '^Game (\d+):'
REGEX_COLOR = '(\d+) %s'

def get_sum_for_game(line):
    print(line)
    for color in TARGETS.keys():
        max_color = 0
        regex = re.compile(REGEX_COLOR % color)
        for match in regex.finditer(line):
            integer_match = int(match.group(1))
            if integer_match > max_color:
                max_color = integer_match
        if max_color > TARGETS[color]:
            return 0
    return int(re.search(REGEX_GAME_NUMBER, line).group(1))


def part_one():
    sum = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            sum = sum + get_sum_for_game(line)
    print(sum)

part_one()

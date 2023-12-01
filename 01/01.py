import re

INPUT_FILE = '01-input.txt'
FIND_FIRST_REGEX = r'(%s).*'
FIND_LAST_REGEX = '.*(%s)'
PART_ONE_SEARCH = '[1-9]{1}'
NUMBERS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def find_number(line, regex):
    matches = re.search(regex, line)
    found_number = str(matches.group(1))
    if found_number in NUMBERS.keys():
        return NUMBERS[found_number]
    else:
        return found_number

def compute_result(regex_first, regex_last):
    sum = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            number = int(find_number(line, regex_first) + find_number(line, regex_last))
            sum += number
    return sum

def part_one():
    find_first_number = FIND_FIRST_REGEX % PART_ONE_SEARCH
    find_last_number = FIND_LAST_REGEX % PART_ONE_SEARCH
    return compute_result(find_first_number, find_last_number)

def part_two():
    numbers = '|'.join(list(NUMBERS.keys())) + '|[0-9]{1}'
    find_first_number = FIND_FIRST_REGEX % numbers
    find_last_number = FIND_LAST_REGEX % numbers
    return compute_result(find_first_number, find_last_number)

print('Part one: ' + str(part_one()))
print('Part two: ' + str(part_two()))

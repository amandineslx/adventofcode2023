import re

INPUT_FILE = '01-input.txt'
FIND_FIRST_NUMBER_REGEX = '[^0-9]*([0-9]{1}).*'
FIND_LAST_NUMBER_REGEX = '.*([0-9]{1})[^0-9]*'

def find_number(line, first=True):
    matches = re.search(FIND_FIRST_NUMBER_REGEX if first else FIND_LAST_NUMBER_REGEX, line)
    return str(matches.group(1))

def main():
    sum = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            number = int(find_number(line, first=True) + find_number(line, first=False))
            sum += number
    return sum

print(main())

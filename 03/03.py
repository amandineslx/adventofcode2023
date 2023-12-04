import re

INPUT_FILE = '03-input.txt'
REGEX_NUMBER = r"\d+"
REGEX_SYMBOL = r"[^0-9.]{1}"

def find_sum_in_line(previous_line, current_line, next_line):
    sum_current_line = 0
    for match in re.finditer(REGEX_NUMBER, current_line):
        index_start = match.start()
        index_end = match.end()
        substring_start = index_start-1 if index_start > 0 else index_start
        substring_end = index_end+1 if index_end < len(current_line)-2 else index_end
        if (len(previous_line) > 0 and re.search(REGEX_SYMBOL, previous_line[substring_start:substring_end])) or re.search(REGEX_SYMBOL, current_line[substring_start:substring_end]) or (len(next_line) > 0 and re.search(REGEX_SYMBOL, next_line[substring_start:substring_end])):
            sum_current_line += int(match.group())
    return sum_current_line

def main():
    previous_line,current_line,next_line = "","",""
    sum_part_one,sum_part_two = 0,0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            previous_line = current_line
            current_line = next_line
            next_line = line
            # we need at least 2 lines to begin
            if not current_line:
                continue
            else:
                sum_part_one += find_sum_in_line(previous_line, current_line, next_line)
        previous_line = current_line
        current_line = next_line
        next_line = ""
        sum_part_one += find_sum_in_line(previous_line, current_line, next_line)
    return sum_part_one

print(main())

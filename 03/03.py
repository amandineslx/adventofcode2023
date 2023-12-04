import re

INPUT_FILE = '03-input.txt'
REGEX_NUMBER = r"\d+"
REGEX_SYMBOL = r"[^0-9.]{1}"
REGEX_STAR = r"\*"

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

class Star:
    def __init__(self):
        self.multiplications = 0
        self.power =  1

    def multiply_power(self, multiplicator):
        self.multiplications += 1
        self.power *= multiplicator

class Stars:
    stars = dict()

    def multiply_power(self, line, index, multiplicator):
        if line not in self.stars:
            self.stars[line] = dict()
        if index not in self.stars[line]:
            self.stars[line][index] = Star()
        self.stars[line][index].multiply_power(multiplicator)

def find_stars(previous_line, current_line, next_line, iterator, stars):
    for match in re.finditer(REGEX_NUMBER, current_line):
        index_start = match.start()
        index_end = match.end()
        substring_start = index_start-1 if index_start > 0 else index_start
        substring_end = index_end+1 if index_end < len(current_line)-2 else index_end
        star_line = None
        if len(previous_line) > 0:
            process_stars_in_line(match, previous_line[substring_start:substring_end], iterator - 1, index_start, stars)
        process_stars_in_line(match, current_line[substring_start:substring_end], iterator, index_start, stars)
        if len(next_line) > 0:
            process_stars_in_line(match, next_line[substring_start:substring_end], iterator + 1, index_start, stars)

def process_stars_in_line(match, substring, star_line, index_start, stars):
    for star in re.finditer(REGEX_STAR, substring):
        star_index = match.start() + star.start()
        if index_start != 0:
            star_index -= 1
        stars.multiply_power(star_line, star_index, int(match.group()))

def process_stars(stars):
    sum = 0
    for line in stars.stars.keys():
        star_line = stars.stars[line]
        for index in star_line.keys():
            star = star_line[index]
            if star.multiplications == 2:
                sum += star.power
    return sum

def main():
    previous_line,current_line,next_line = "","",""
    sum_part_one = 0
    stars = Stars()
    with open(INPUT_FILE, 'r') as f:
        iterator = 0
        for line in f.readlines():
            previous_line = current_line
            current_line = next_line
            next_line = line
            # we need at least 2 lines to begin
            if not current_line:
                continue
            else:
                sum_part_one += find_sum_in_line(previous_line, current_line, next_line)
                find_stars(previous_line, current_line, next_line, iterator, stars)
                iterator += 1
        previous_line = current_line
        current_line = next_line
        next_line = ""
        sum_part_one += find_sum_in_line(previous_line, current_line, next_line)
        find_stars(previous_line, current_line, next_line, iterator, stars)
    return sum_part_one, process_stars(stars)

print(main())

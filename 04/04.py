import re

INPUT_FILE = '04-input.txt'

def get_number_of_winning_numbers(line):
    winning_numbers = 0
    numbers = line.split(":")[1]
    winning_numbers_s, played_numbers_s = numbers.split("|")
    winning_numbers_l = winning_numbers_s.split(" ")
    for played_number in played_numbers_s.split(" "):
        if played_number and played_number in winning_numbers_l:
            winning_numbers += 1
    return winning_numbers

def get_ticket_value(line):
    ticket_value = 0
    numbers = line.split(":")[1]
    winning_numbers_s, played_numbers_s = numbers.split("|")
    winning_numbers_l = winning_numbers_s.split(" ")
    for played_number in played_numbers_s.split(" "):
        if played_number and played_number in winning_numbers_l:
            if ticket_value == 0:
                ticket_value = 1
            else:
                ticket_value *=2
    return ticket_value

def main():
    sum_part_one,sum_part_two = 0,0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            sum_part_one += get_ticket_value(line[:-1])
            sum_part_two += 1 + get_number_of_winning_numbers(line[:-1])
    return sum_part_one,sum_part_two

print(main())

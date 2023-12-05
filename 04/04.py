import re

INPUT_FILE = '04-input.txt'
TICKETS = dict()
REGEX_CARD_NUMBER = '^Card[ ]*(\d+):'

def add_ticket_copies(ticket_number, copies):
    if ticket_number not in TICKETS:
        TICKETS[ticket_number] = copies
    else:
        TICKETS[ticket_number] += copies

def get_number_of_winning_numbers(line):
    winning_numbers = 0
    numbers = line.split(":")[1]
    winning_numbers_s, played_numbers_s = numbers.split("|")
    winning_numbers_l = winning_numbers_s.split(" ")
    for played_number in played_numbers_s.split(" "):
        if played_number and played_number in winning_numbers_l:
            winning_numbers += 1
    return winning_numbers

def process_ticket(line):
    card_number = re.search(REGEX_CARD_NUMBER, line).group(1)
    add_ticket_copies(card_number, 1)
    card_copies = TICKETS[card_number]
    winning_numbers = get_number_of_winning_numbers(line)
    if winning_numbers:
        for i in range(winning_numbers):
            add_ticket_copies(str(int(card_number) + i + 1), card_copies)

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
    sum_part_one = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            sum_part_one += get_ticket_value(line[:-1])
            process_ticket(line[:-1])
    return sum_part_one,sum(TICKETS.values())

print(main())

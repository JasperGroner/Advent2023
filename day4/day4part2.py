import sys
from dataclasses import dataclass

from day4part1 import make_line_array, get_numbers_from_string

@dataclass
class ScratchCard:
    """Class for keeping track of scratch card winning numbers and quantity"""
    number_of_matches: int
    card_quantity: int

def make_initial_digest(scratch_card_array):
    """Create initial digest of cards"""
    scratch_card_digest = []
    for scratch_card in scratch_card_array:
        [game_string, number_string] = scratch_card.split(':')
        [winning_number_string, your_numbers_string] = number_string.split('|')
        winning_number_set = set(get_numbers_from_string(winning_number_string))
        your_numbers_list = get_numbers_from_string(your_numbers_string)
        number_of_matches = 0
        for number in your_numbers_list:
            if number in winning_number_set:
                number_of_matches += 1
        scratch_card_digest.append(ScratchCard(number_of_matches, 1))
    
    return scratch_card_digest

def process_scratch_card(scratch_card_number, scratch_card_digest):
    """Update number of scratch cards and digest any new cards """
    scratch_card = scratch_card_digest[scratch_card_number]
    for i in range(scratch_card_number + 1, scratch_card_number + scratch_card.number_of_matches + 1):
        scratch_card_digest[i].card_quantity += scratch_card.card_quantity
    
def main(argv):
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    scratch_card_array = make_line_array(input_file_name)

    number_of_scratch_cards = 0
    
    scratch_card_digest = make_initial_digest(scratch_card_array)

    for i in range(0, len(scratch_card_digest)):
        process_scratch_card(i, scratch_card_digest)

    for card in scratch_card_digest:
        number_of_scratch_cards += card.card_quantity

    print(number_of_scratch_cards)

    return number_of_scratch_cards


if __name__ == '__main__':
    main(sys.argv[1:])

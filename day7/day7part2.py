import sys
from dataclasses import dataclass

CARD_VALUES = {
    "J": '0',
    "2": '1',
    "3": '2',
    "4": '3',
    "5": '4',
    "6": '5',
    "7": '6',
    "8": '7',
    "9": '8',
    "T": '9',
    "Q": 'b',
    "K": 'c',
    "A": 'd'
}

@dataclass
class ProcessedHand:
    """
        Store sortable string for hand and bid value
    """
    hand_string: str
    bid: int

def make_line_array(input_file_name):
    """
        Take an input file and return
        array of the lines in the file.
    """

    file_reader = open(input_file_name, 'r')
    raw_input = file_reader.read()
    line_array = raw_input.splitlines()

    file_reader.close()
    return line_array

def get_hand_category(hand):
    """
        Get the category the hand falls in.
    """
    card_count = {}
    for char in hand:
        if char not in card_count:
            card_count[char] = 1
        else:
            card_count[char] += 1
    num_jokers = 0
    if 'J' in card_count:
        num_jokers = card_count['J']
        # Edge case for 5 joker hand - no other cards to add them to
        if num_jokers == 5:
            return '7'
        del card_count['J']
    matches = list(card_count.values())
    # Add joker # to the highest card aount will always result in the best hands
    max_match = max(matches)
    max_match_idx = matches.index(max_match)
    matches[max_match_idx] += num_jokers
    # Get sortable value for first char of procerssed hand from most valuable to least
    if 5 in matches:
        return '7'
    if 4 in matches:
        return '6'
    if 3 in matches:
        if 2 in matches:
            return '5'
        return '4'
    if 2 in matches:
        matches.remove(2)
        if 2 in matches:
            return '3'
        return '2'
    return '1'
        

def process_hand(string):
    """
        Convert hand to ProcessedHand
    """

    hand, bid = string.split(" ")
    print("hand: " + hand)
    bid = int(bid)
    hand_string = get_hand_category(hand)
    for char in hand:
        hand_string += CARD_VALUES[char]
    print(hand_string)
    return ProcessedHand(hand_string, bid)


def main(argv):
    """
        What do you think main does?
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    card_lines = make_line_array(input_file_name)

    processed_hands = []

    for card in card_lines:
        processed_hands.append(process_hand(card))

    processed_hands.sort(key=lambda x: x.hand_string)

    answer = 0

    for index, processed_hand in enumerate(processed_hands):
        answer += (index + 1) * processed_hand.bid

    print(answer)
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

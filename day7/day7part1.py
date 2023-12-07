import sys
from dataclasses import dataclass

CARD_VALUES = {
    "2": '1',
    "3": '2',
    "4": '3',
    "5": '4',
    "6": '5',
    "7": '6',
    "8": '7',
    "9": '8',
    "T": '9',
    "J": 'a',
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
    card_count = {}
    for char in hand:
        if char not in card_count:
            card_count[char] = 1
        else:
            card_count[char] += 1
    matches = list(card_count.values())
    if 5 in matches:
        return '7'
    if 4 in matches:
        return '6'
    if 3 in matches and 2 in matches:
        return '5'
    if 3 in matches:
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
    bid = int(bid)
    hand_string = get_hand_category(hand)
    for char in hand:
        hand_string += CARD_VALUES[char]
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

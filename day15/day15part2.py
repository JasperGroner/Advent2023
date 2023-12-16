import sys
from day15part1 import get_inputs, hash_input

def index_of_label(box: list[str], label: str) -> int:
    """
        returns index of item with label if it's in the box or
        -1 if not
    """
    existing = [index for index, item in enumerate(box) if item.startswith(label)]
    if existing:
        return existing[0]
    return -1


def make_hash_map(unhashed_instructions: list[str]) -> dict:
    """
        Turn list of inputs into hashmap
        using alogrithm from problem
    """
    hash_map = {}
    for instruction in unhashed_instructions:
        if "=" in instruction:
            [label, lens] = instruction.split("=")
            box = hash_input(label)
            insertion = " ".join([label, lens])
            if box not in hash_map:
                hash_map[box] = [insertion]
            else:
                existing = index_of_label(hash_map[box], label)
                if existing != -1:
                    hash_map[box][existing] = insertion
                else:
                    hash_map[box].append(insertion)
        elif "-" in instruction:
            label = instruction[:-1]
            box = hash_input(label)
            if box in hash_map:
                existing = index_of_label(hash_map[box], label)
                if existing != -1:
                    del hash_map[box][existing]

    return hash_map

def get_item_value(box: str, contents: list[str]) -> int:
    """
        get focusing power of box 
    """
    value = 0
    box_number = int(box) + 1
    for idx, item in enumerate(contents):
        value += box_number * (idx + 1) * int(item[-1:])
    return value

def main(argv: list[str]) -> int:
    """
        it's main it does the main stuff
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    inputs = get_inputs(input_file_name)

    hash_map = make_hash_map(inputs)
    
    answer = 0

    for box, contents in hash_map.items():
        answer += get_item_value(box, contents)

    print("answer: " + str(answer))
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

import sys

from day9part1 import make_line_array

def get_prev_item(line):
    """
        Recurse to get prevs item in list
    """
    if any(line):
        next_line = [line[idx + 1] - item
                    for idx, item in enumerate(line)
                    if idx < len(line) - 1]
        return line[0] - get_prev_item(next_line)
    return 0


def get_answer(line_array):
    """
        Get next value in input array
    """
    total = 0
    for line in line_array:
        integer_list = [int(item) for item in line.split(" ")]
        total += get_prev_item(integer_list)
    return total

def main(argv):
    """
        What do you think main does?
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    line_array = make_line_array(input_file_name)

    answer = get_answer(line_array)

    print(answer)
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

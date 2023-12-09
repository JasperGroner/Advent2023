import sys

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

def get_next_item(line):
    """
        Recurse to get next item in list
    """
    if any(line):
        next_line = [line[idx + 1] - item
                    for idx, item in enumerate(line)
                    if idx < len(line) - 1]
        return line[-1] + get_next_item(next_line)
    return 0


def get_answer(line_array):
    """
        Get next value in input array
    """
    total = 0
    for line in line_array:
        integer_list = [int(item) for item in line.split(" ")]
        total += get_next_item(integer_list)
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


import sys

def make_line_array(input_file_name):
    """
        Take an input file and return
        array of the lines in the file.
    """
    line_array = []

    file_reader = open(input_file_name, 'r')
    raw_input = file_reader.read()
    line_array = raw_input.splitlines()

    file_reader.close()
    return line_array

def get_numbers_from_string(input_string):
    """
        Get numbers from string of spaces and numbers.
    """
    number_list = []
    curr_num = ''
    for char in input_string:
        if char.isdigit():
            curr_num += char
        elif curr_num:
            number_list.append(curr_num)
            curr_num = ''
    if curr_num:
        number_list.append(curr_num)
    return number_list

def get_winning_number_set(winning_number_string):
    """
       Get a winning number set from a string of the first
       half of a line. 
    """
    raw_numbers_string = winning_number_string.split(": ")[1]
    winning_number_set = set(get_numbers_from_string(raw_numbers_string))
    return winning_number_set


def get_line_point_value(line):
    """
        Get the point value for a given line.
    """
    points = 0
    [winning_number_string, your_numbers_string] = line.split("|")
    winning_number_set = get_winning_number_set(winning_number_string)
    your_numbers_list = get_numbers_from_string(your_numbers_string)
    for number in your_numbers_list:
        if number in winning_number_set:
            points = 1 if not points else points * 2
    return points

def main(argv):
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    line_array = make_line_array(input_file_name)

    total_points = 0

    for line in line_array:
        total_points += get_line_point_value(line)

    print(total_points)
    return total_points


if __name__ == '__main__':
    main(sys.argv[1:])

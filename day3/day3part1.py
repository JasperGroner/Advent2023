import sys

def make_line_array(input_file_name):
    """
        Take an input file and return
        array of the lines in the file.
    """
    line_array = []

    file_reader = open(input_file_name, 'r')
    raw_input = file_reader.read()
    raw_input_lines = raw_input.splitlines()

    for line in raw_input_lines:
        line_array.append(line)
    
    file_reader.close()
    return line_array


def check_if_symbol(char):
    """
        checks for non-dot, non-digital chars
    """
    return (not char.isdigit()) and (char != '.')

def check_if_part_number(line_array, y_coord, x_coord_start, num_length):
    """
        Checks to see if symbols are adjacent to number and thus if it is a part number
    """
    is_part_number = False
    for y in range(y_coord - 1, y_coord + 2):
        for x in range(x_coord_start - 1, x_coord_start + num_length + 1):
            if (y > -1 and y < len(line_array)) and (x > -1 and x < len(line_array[y])):
                if check_if_symbol(line_array[y][x]):
                    return True
    return is_part_number


def get_part_numbers(line_array):
    """
        Take an array of lines and get
        part numbers - where number adjoins non-digit
    """
    part_numbers = []
    for y, line in enumerate(line_array):
        num = ''
        start_x = None
        for x, char in enumerate(line):
            if char.isdigit():
                num += char
                if (start_x is None):
                    start_x = x
            elif num:
                if check_if_part_number(line_array, y, start_x, len(num)):
                    part_numbers.append(num)
                num = ''
                start_x = None
        # test for endlines
        if num and check_if_part_number(line_array, y, start_x, len(num)):
            part_numbers.append(num)
            start_x = None
    return part_numbers



def main(argv):
    if len(argv) < 1:
        print("Please include file input")
        return
    input_file_name = argv[0]

    line_array = make_line_array(input_file_name)
    part_numbers = get_part_numbers(line_array)
    sum_part_numbers = 0

    for part_number in part_numbers:
        sum_part_numbers += int(part_number)
    print(sum_part_numbers)
    return(sum_part_numbers)

if __name__ == '__main__':
    main(sys.argv[1:])

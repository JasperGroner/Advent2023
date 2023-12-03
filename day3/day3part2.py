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

def get_full_num(line_array, y_loc, x_loc):
    """
        Get number from any digit
    """
    number = ''
    current_x = x_loc
    while current_x < len(line_array) and line_array[y_loc][current_x].isdigit():
        number += line_array[y_loc][current_x]
        current_x += 1
    current_x = x_loc - 1
    while current_x >= 0 and line_array[y_loc][current_x].isdigit():
        number = line_array[y_loc][current_x] + number
        current_x -= 1
    return int(number)


def get_adjacent_parts_product(line_array, y_loc, x_loc):
    """
        Gets all adjacent parts numbers
    """
    adjacent_part_numbers = []
    for y in range(y_loc - 1, y_loc + 2):
        current_num = ''
        for x in range(x_loc - 1, x_loc + 2):
            if 0 <= y < len(line_array) and 0 <= x < len(line_array[y]):
                if line_array[y][x].isdigit():
                    current_num += line_array[y][x]
                elif current_num:
                    current_num = ''
                    adjacent_part_numbers.append(get_full_num(line_array, y, x - 1))
        if current_num:
            adjacent_part_numbers.append(get_full_num(line_array, y, x_loc + 1))
    if len(adjacent_part_numbers) == 2:
        return adjacent_part_numbers[0] * adjacent_part_numbers[1]
    return 0


def get_gear_numbers(line_array):
    """
        Take an array of lines and get
        part numbers - where number adjoins non-digit
    """
    gear_numbers = []
    for y, line in enumerate(line_array):
        for x, char in enumerate(line):
            if char == '*':
                product = get_adjacent_parts_product(line_array, y, x)
                if product:
                    gear_numbers.append(product)
    return gear_numbers



def main(argv):
    if len(argv) < 1:
        print("Please include file input")
        return
    input_file_name = argv[0]

    line_array = make_line_array(input_file_name)
    part_numbers = get_gear_numbers(line_array)
    sum_part_numbers = 0

    for part_number in part_numbers:
        sum_part_numbers += int(part_number)
    print(sum_part_numbers)
    return(sum_part_numbers)

if __name__ == '__main__':
    main(sys.argv[1:])

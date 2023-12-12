import sys

def make_line_array(input_file_name: str) -> list[str]:
    """
        Take an input file and return
        array of the lines in the file.
    """

    with open(input_file_name, 'r') as file_reader:
        raw_input = file_reader.read()
        line_array = raw_input.splitlines()

        return line_array

def process_input(raw_input: list[str]):
    """
        process input into lists of possible spaces
        and required spaces
    """
    processed_data = []
    for line in raw_input:
        map_row, required_locs = line.split(" ")
        required_locs = tuple(required_locs.split(","))
        processed_data.append([map_row, required_locs])
    return processed_data

def get_perms(line, depth):
    """
        get permutations of line
    """
    if depth == 0:
        print(line, depth)
    map_row, required_locs = line
    if len(required_locs) == 0:
        if "#" not in map_row:
            # print("valid loc")
            # got all required locations and none left - valid permutation
            return 1
        return 0
    current_size = int(required_locs[0])
    permutations = 0
    for loc, char in enumerate(map_row):
        valid_loc = True
        if loc + current_size > len(map_row):
            # We've gotten past the end of the row
            break
        if "#" in map_row[:loc]:
            # If we've gone beyond a required #, break
            break
        for i in range(current_size):
            # There's not an available number of possible spaces
            if map_row[loc + i] not in ("?", "#"):
                # print("out of space")
                valid_loc = False

        if loc + current_size < len(map_row) and map_row[loc + current_size] == "#":
            # The next space is required and would be blank
            # print("next space required")
            valid_loc = False
        if valid_loc:
            # Get remaining permutations
            if loc + current_size <= len(map_row):
                permutations += get_perms([map_row[loc + current_size + 1:], required_locs[1:]], depth + 1)
    return permutations

def get_five_fold_perms(line):
    permutations = get_perms(line, 0)

    positions_can_shift_right = 0


    while positions_can_shift_right < len(line[0]):
        if (get_perms([line[0][positions_can_shift_right + 1:], line[1]], 0)):
            positions_can_shift_right += 1
        else:
            break
    
    positions_can_shift_left = 0


    while positions_can_shift_left < len(line[0]):
        if (get_perms([line[0][:-(positions_can_shift_left + 1)], line[1]], 0)):
            positions_can_shift_left += 1
        else:
            break


    print(positions_can_shift_right, positions_can_shift_left)

    return permutations

    # permutations_one_after, permutations_one_before = permutations, permutations

    # permutations_one_after = get_perms([line[0] + "?", line[1]], 0)

    # permutations_one_before = get_perms(["?" + line[0], line[1]], 0)

    # return permutations * (pow(max([permutations_one_after, permutations_one_before ]), 4))

def main(argv):
    """
        What do you think main does?
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    raw_input = make_line_array(input_file_name)

    processed_input = process_input(raw_input)

    answer = 0

    for line in processed_input:
        print(line)
        adds = get_five_fold_perms(line)
        print(adds)
        answer += adds

    print(answer)
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

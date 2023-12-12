import sys

stored_permutations = {}

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
        required_locs = tuple(required_locs.split(",") * 5)
        processed_data.append(((map_row + "?") * 4 + map_row, required_locs))
    return processed_data

def get_perms(line, depth):
    """
        get permutations of line
    """
    if line in stored_permutations:
        return stored_permutations[line]
    # print(line, depth)
    map_row, required_locs = line
    if len(required_locs) == 0:
        return 0
    current_size = int(required_locs[0])
    permutations = 0
    for loc in range(len(map_row)):
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
                break

        if loc + current_size < len(map_row) and map_row[loc + current_size] == "#":
            # The next space is required and would be blank
            # print("next space required")
            valid_loc = False
        if valid_loc:
            # Get remaining permutations
            if loc + current_size <= len(map_row):
                if (len(required_locs[1:]) == 0 and ("#" not in map_row[loc + current_size + 1:])):
                    permutations += 1
                else:
                    new_line = (map_row[loc + current_size + 1:], required_locs[1:])
                    new_perms = get_perms(new_line, depth + 1)
                    stored_permutations[new_line] = new_perms
                    permutations += new_perms
    return permutations


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
        adds = get_perms(line, 0)
        answer += adds
    
    print(len(stored_permutations.keys()))

    print("answer: " + str(answer))
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

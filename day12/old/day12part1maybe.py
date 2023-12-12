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

def get_entry(last_char, last_char_count):
    return [last_char + str(last_char_count)]

def process_map(map_row):
    """
        process map into list
    """
    processed_map = []
    last_char = ""
    last_char_count = 0
    for char in map_row:
        if char == last_char:
            last_char_count += 1
        else:
            if last_char:
                processed_map += [(last_char, last_char_count)]
            last_char = char
            last_char_count = 1
    processed_map += [(last_char, last_char_count)]
    return processed_map

def process_input(raw_input: list[str]):
    """
        process input into lists of possible spaces
        and required spaces
    """
    processed_data = []
    for line in raw_input:
        map_row, required_locs = line.split(" ")
        required_locs = tuple(required_locs.split(","))
        processed_data.append([process_map(map_row), required_locs])
    return processed_data

def get_perms(line):
    print(line)
    processed_map, required_locs = line
    permutations = 0
    if len(required_locs) == 1:
        chunk_length = 0
        for chunk in processed_map:
            if chunk[0] == ".":
                return 0
    return 0

# def get_perms(line, depth):
#     """
#         get permutations of line
#     """
#     # print(line, depth)
#     map_row, required_locs = line
#     if len(required_locs) == 0:
#         if "#" not in map_row:
#             # print("valid loc")
#             # got all required locations and none left - valid permutation
#             return 1
#         return 0
#     current_size = int(required_locs[0])
#     permutations = 0
#     for loc, char in enumerate(map_row):
#         valid_loc = True
#         if loc + current_size > len(map_row):
#             # We've gotten past the end of the row
#             break
#         if "#" in map_row[:loc]:
#             # If we've gone beyond a required #, break
#             break
#         for i in range(current_size):
#             # There's not an available number of possible spaces
#             if map_row[loc + i] not in ("?", "#"):
#                 # print("out of space")
#                 valid_loc = False

#         if loc + current_size < len(map_row) and map_row[loc + current_size] == "#":
#             # The next space is required and would be blank
#             # print("next space required")
#             valid_loc = False
#         if valid_loc:
#             # Get remaining permutations
#             if loc + current_size <= len(map_row):
#                 permutations += get_perms([map_row[loc + current_size + 1:], required_locs[1:]], depth + 1)
#     return permutations


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
        adds = get_perms(line)
        print(adds)
        answer += adds

    print(answer)
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

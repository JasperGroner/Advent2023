import sys

from day10part1 import make_line_array, find_start, get_first_steps, EXITS, Pipe

def get_start_char(first_steps):
    openings = []
    for pipe in first_steps:
        if pipe.location["x"] - pipe.prev_pipe["x"] == 1:
            openings.append("+x")
        elif pipe.location["x"] - pipe.prev_pipe["x"] == -1:
            openings.append("-x")
        elif pipe.location["y"] - pipe.prev_pipe["y"] == 1:
            openings.append("+y")
        else:
            openings.append("-y")
    
    for key, value in EXITS.items():
        if value == openings:
            return key

def get_clean_line_array(line_array, pipes, start_y, start_x):
    clean_line_array = []
    for idx, line in enumerate(line_array):
        clean_line_array.append([])
        for char in line:
            clean_line_array[idx].append(".")
    
    clean_line_array[start_y][start_x] = get_start_char(pipes)

    while (pipes[0].location["x"] != pipes[1].location["x"] or pipes[0].location["y"] != pipes[1].location["y"]):
        for idx, pipe in enumerate(pipes):
            clean_line_array[pipe.location["y"]][pipe.location["x"]] = pipe.char
            prev_x, prev_y = pipe.location["x"], pipe.location["y"]
            pipes[idx] = Pipe(x = pipe.next_pipe["x"], y = pipe.next_pipe["y"],
                char = line_array[pipe.next_pipe["y"]][pipe.next_pipe["x"]])
            pipes[idx].set_prev_pipe(prev_x, prev_y)
            pipes[idx].get_next_pipe()

    clean_line_array[pipes[0].location["y"]][pipes[0].location["x"]] = pipes[0].char

    return clean_line_array


def is_interior(y, x, clean_line_array):
    if clean_line_array[y][x] != '.':
        return False
    
    left, right = 0, 0
    for y_loc in range(y, -1, -1):
        char = clean_line_array[y_loc][x]
        if char in ["-", "L", "F"]:
            right += 1

    return right % 2 == 1


def get_number_of_interior_spaces(clean_line_array):
    number = 0
    for y, line in enumerate(clean_line_array):
        for x, char in enumerate(line):
            number += 1 if is_interior(y, x, clean_line_array) else 0
    return number


def main(argv):
    """
        What do you think main does?
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    line_array = make_line_array(input_file_name)

    start_y, start_x = find_start(line_array)

    first_steps = get_first_steps(line_array, start_y, start_x)

    clean_line_array = get_clean_line_array(line_array, first_steps, start_y, start_x)

    answer = get_number_of_interior_spaces(clean_line_array)
    
    print(answer)
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

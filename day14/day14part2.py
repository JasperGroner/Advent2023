import sys
from day14part1 import make_line_array, get_answer

def move_rocks_cycle(raw_input: list[list[str]]) -> list[list[str]]:
    """
        Make rocks roll north on a pattern that has been rotated ninety degrees
        so that north is the end of each row of the pattern
    """
    transformed = [row[:] for row in raw_input]
    cycle = ["north", "west", "south", "east"]
    for current_cycle in cycle:
        for i, line in enumerate(transformed):
            for j, _ in enumerate(line):
                mod_i = i if current_cycle in ("north", "west") else len(transformed) - 1 - i

                mod_j = j if current_cycle in ("north", "west") else len(line) - 1 - j

                if transformed[mod_i][mod_j] in (".", "#"):
                    continue

                current = mod_i if current_cycle in ("north", "south") else mod_j

                if current_cycle == "north":
                    while current - 1 >= 0 and transformed[current - 1][mod_j] == ".":
                        current -= 1
                elif current_cycle == "west":
                    while current - 1 >= 0 and transformed[mod_i][current - 1] == ".":
                        current -= 1
                elif current_cycle == "south":
                    while current + 1 < len(transformed) and transformed[current + 1][mod_j] == ".":
                        current += 1
                elif current_cycle == "east":
                    while current + 1 < len(transformed[0]) and transformed[mod_i][current + 1] == ".":
                        current += 1
                
                if current_cycle in ("north", "south"):
                    transformed[mod_i][mod_j] = '.'
                    transformed[current][mod_j] = 'O'
                else:
                    transformed[mod_i][mod_j] = '.'
                    transformed[mod_i][current] = 'O'

    return transformed

def find_final_pattern(raw_input):
    """
        determine any cycles in raw input
    """
    current_pattern = [row[:] for row in raw_input]

    stored_cycle_results = []

    begin_cycle, cycle_length = 0, 0

    for i in range(1000000000):
        new_pattern = move_rocks_cycle(current_pattern)
        if new_pattern in stored_cycle_results:
            begin_cycle = stored_cycle_results.index(new_pattern)
            cycle_length = i - begin_cycle
            break
        stored_cycle_results.append(new_pattern)
        current_pattern = [row[:] for row in new_pattern]

    # -1 because 0 indexing - the 10th cycle is at loc #9, etc.
    location = (1000000000 - 1 - begin_cycle) % (cycle_length)

    return stored_cycle_results[begin_cycle + location]

def main(argv: list[str]) -> int:
    """
        it's main it does the main stuff
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    raw_input = make_line_array(input_file_name)

    transformed = find_final_pattern(raw_input)

    answer = get_answer(transformed)

    print("answer: " + str(answer))
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

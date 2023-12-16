import sys
import time
from day16part1 import make_line_array, follow_light

def get_blank_light_map(mirror_map: list[list[str]]) -> list[list[str]]:
    """
        returns blank light map
    """
    light_map = []

    for idx, row in enumerate(mirror_map):
        light_map.append([])
        for _ in row:
            light_map[idx].append('')

    return light_map

def get_cells_activated(light_map: list[list[str]]) -> int:
    """
        gets number of activated cells
    """
    answer = 0

    for row in light_map:
        for char in row:
            if char:
                answer += 1

    return answer

def main(argv: list[str]) -> int:
    """
        it's main it does the main stuff
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    start_time = time.time()
    input_file_name = argv[0]

    mirror_map = make_line_array(input_file_name)

    max_answer = 0

    for idx, row in enumerate(mirror_map):
        for direction, start in [('R', (idx, 0)), ('L', (idx, len(row) - 1))]:
            blank_light_map = get_blank_light_map(mirror_map)

            light_map = follow_light(mirror_map, blank_light_map, direction, start)
            answer = get_cells_activated(light_map)
            max_answer = answer if answer > max_answer else max_answer

    for idx, _ in enumerate(mirror_map[0]):
        for direction, start in [('D', (0, idx)), ('U', (len(mirror_map) - 1, idx))]:
            blank_light_map = get_blank_light_map(mirror_map)

            light_map = follow_light(mirror_map, blank_light_map, direction, start)
            answer = get_cells_activated(light_map)
            max_answer = answer if answer > max_answer else max_answer

    print("answer: " + str(max_answer))

    end_time = time.time()

    print(end_time - start_time)
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

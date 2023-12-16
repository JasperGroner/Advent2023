import sys

def make_line_array(input_file_name: str) -> list[str]:
    """
        Take an input file and return
        array of the lines, with each character as a cell
    """

    with open(input_file_name, 'r') as file_reader:
        raw_input = file_reader.read()
        line_array = raw_input.splitlines()
        
        for idx, line in enumerate(line_array):
            line_array[idx] = [*line]

        return line_array

def follow_light(mirror_map: list[list[str]], light_map: list[list[str]], direction: str, location: tuple):
    """
        Follow a beam of light and map its direction and location on
        light_map
    """
    # light_map = [line[:] for line in light_map_param]

    y, x = location

    while True:
        if x < 0 or x > len(light_map[0]) - 1 or y < 0 or y > len(light_map) - 1:
            break

        if (direction not in light_map[y][x]):
            light_map[y][x] = light_map[y][x] + direction
        else:
            break
        
        if mirror_map[y][x] == "/":
            direction = "U" if direction == "R" else \
                "D" if direction == "L" else \
                "R" if direction == "U" else "L"
        elif mirror_map[y][x] == "\\":
            direction = "U" if direction == "L" else \
                "D" if direction == "R" else \
                "R" if direction == "D" else "L"
        elif mirror_map[y][x] == "|" and direction in ("L", "R"):
            direction = "U"
            light_map = follow_light(mirror_map, light_map, "D", (y + 1, x))
        elif mirror_map[y][x] == "-" and direction in ("U", "D"):
            direction = "L"
            light_map = follow_light(mirror_map, light_map, "R", (y, x + 1))

        if direction == "R":
            x += 1
        elif direction == "L":
            x -= 1
        elif direction == "D":
            y += 1
        elif direction == "U":
            y -= 1
    
    return light_map


def main(argv: list[str]) -> int:
    """
        it's main it does the main stuff
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    mirror_map = make_line_array(input_file_name)

    light_map = []

    for idx, row in enumerate(mirror_map):
        light_map.append([])
        for _ in row:
            light_map[idx].append('')


    light_map = follow_light(mirror_map, light_map, 'R', (0, 0))

    answer = 0

    for row in light_map:
        for char in row:
            if char:
                answer += 1


    print("answer: " + str(answer))
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

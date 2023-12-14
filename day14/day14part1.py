import sys

def make_line_array(input_file_name: str) -> list[str]:
    """
        Take an input file and return
        array of the lines in the file.
    """

    with open(input_file_name, 'r') as file_reader:
        raw_input = file_reader.read()
        line_array = raw_input.splitlines()
        
        for idx, line in enumerate(line_array):
            line_array[idx] = [*line]

        return line_array

def move_rocks_north(rotated: list[list[str]]) -> list[list[str]]:
    """
        Make rocks roll north on a pattern that has been rotated ninety degrees
        so that north is the end of each row of the pattern
    """
    rocks_north = [row[:] for row in rotated]
    for i, line in enumerate(rocks_north):
        for j, char in enumerate(line):
            if char in (".", "#"):
                continue
            current = i

            while current - 1 >= 0 and rocks_north[current - 1][j] == ".":
                current -= 1

            rocks_north[i][j] = '.'
            rocks_north[current][j] = 'O'
    return rocks_north

def get_answer(transformed: list[list[str]]) -> int:
    """
        Get weight of rocks to north in rotated and transformed pattern
    """
    answer = 0
    for idx, line in enumerate(transformed):
        for char in line:
            if char == "O":
                answer += (len(transformed) - idx)
    return answer

def main(argv: list[str]) -> int:
    """
        it's main it does the main stuffd
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    raw_input = make_line_array(input_file_name)

    transformed = move_rocks_north(raw_input)

    answer = get_answer(transformed)

    print("answer: " + str(answer))
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

import sys
from day13part1 import make_line_array, process_input, MirrorPattern

def is_smudge_mirror(first, second):
    """
        swap character and check for equality
    """
    for idx, char in enumerate(first):
        swapped_char = "#" if char == "." else "."
        altered_first = first[:idx] + swapped_char + first[idx + 1:]
        if altered_first == second:
            return True
    return False

def get_flip_point(pattern: list[str]):
    """
        returns the flip point of a pattern
    """
    for idx, _ in enumerate(pattern):
        if idx == len(pattern) - 1:
            continue
        offset = 0
        is_mirror = True
        has_smudge = False
        while idx - offset >= 0 and idx + offset + 1 < len(pattern):
            first, second = pattern[idx - offset], pattern[idx + offset + 1]
            if first != second:
                if not has_smudge and is_smudge_mirror(first, second):
                    has_smudge = True
                else:
                    is_mirror = False
                    break
            offset += 1
        if is_mirror and has_smudge:
            return idx + 1
    return 0

def get_value(mirror_pattern: MirrorPattern):
    """
        Returns the value of a mirror pattern
    """
    return horizontal_result if (horizontal_result := get_flip_point(mirror_pattern.horizontal)) else get_flip_point(mirror_pattern.vertical) * 100


def main(argv):
    """
        it's main it does the main stuffd
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    raw_input = make_line_array(input_file_name)

    processed_input = process_input(raw_input)

    answer = 0

    for mirror_pattern in processed_input:
        answer += get_value(mirror_pattern)
    
    print("answer: " + str(answer))
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

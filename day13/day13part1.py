import sys
from dataclasses import dataclass

@dataclass
class MirrorPattern:
    vertical: list[str]
    horizontal: list[str]

def make_line_array(input_file_name: str) -> list[str]:
    """
        Take an input file and return
        array of the lines in the file.
    """

    with open(input_file_name, 'r') as file_reader:
        raw_input = file_reader.read()
        line_array = raw_input.splitlines()

        return line_array

def get_rotated(pattern: list[str]) -> list[str]:
    """
        Rotate pattern on vertical axis
    """
    rotated_pattern: list[str] = []
    for line in pattern:
        for column, char in enumerate(line):
            if len(rotated_pattern) < len(line):
                rotated_pattern.append("")
            new_str = rotated_pattern[column]
            rotated_pattern[column] = new_str + char
    return rotated_pattern

def process_input(raw_input: list[str]) -> list[MirrorPattern]:
    """
        Transform raw input into easily digestible MirrorPatterns
    """
    current_pattern: list[str] = []
    all_patterns: list[list[str]] = []
    for line in raw_input:
        if line != '':
            current_pattern.append(line)
        else:
            all_patterns.append(current_pattern)
            current_pattern = []
    
    all_patterns.append(current_pattern)

    processed_patterns: list[MirrorPattern] = []

    for pattern in all_patterns:
        rotated = get_rotated(pattern)
        processed_patterns.append(MirrorPattern(pattern, rotated))
        
    return processed_patterns

def get_flip_point(pattern: list[str]) -> int:
    """
        returns the flip point of a pattern
    """
    for idx, _ in enumerate(pattern):
        if idx == len(pattern) - 1:
            continue
        offset = 0
        is_mirror = True
        while idx - offset >= 0 and idx + offset + 1 < len(pattern):
            if pattern[idx - offset] != pattern[idx + offset + 1]:
                is_mirror = False
                break
            offset += 1
        if is_mirror:
            return idx + 1
    return 0

def get_value(mirror_pattern: MirrorPattern) -> int:
    """
        Returns the value of a mirror pattern
    """
    return horizontal_result if (horizontal_result := get_flip_point(mirror_pattern.horizontal)) else get_flip_point(mirror_pattern.vertical) * 100


def main(argv: list[str]) -> int:
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

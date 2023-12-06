import sys
import re

from day6part1 import get_ways_to_win, Race

def get_race_info(input_file_name):
    """
        Gets the race info from the input file
    """
    file_reader = open(input_file_name, 'r')
    raw_input = file_reader.read()
    [duration_line, record_length_line] = raw_input.splitlines()
    duration = "".join(re.findall(r"\d+", duration_line))
    record_length = "".join(re.findall(r"\d+", record_length_line))

    return Race(int(duration), int(record_length))


def main(argv):
    """
        What do you think main does?
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    race = get_race_info(input_file_name)

    answer = get_ways_to_win(race)

    print(answer)
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

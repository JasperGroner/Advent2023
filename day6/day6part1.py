import sys
import re
from dataclasses import dataclass

@dataclass
class Race:
    """
        Stores race duration and record length
    """
    duration: int
    record_length: int

def make_line_array(input_file_name):
    """
        Take an input file and return
        array of the lines in the file.
    """
    line_array = []

    file_reader = open(input_file_name, 'r')
    raw_input = file_reader.read()
    line_array = raw_input.splitlines()

    file_reader.close()
    return line_array

def make_race_array(line_array):
    """
        Take an array of input lines and turn it
        into Race objects
    """
    race_array = []
    durations = re.findall(r"\d+", line_array[0])
    record_lengths = re.findall(r"\d+", line_array[1])

    for i, duration in enumerate(durations):
        race_array.append(Race(int(duration), int(record_lengths[i])))

    return race_array

def is_way_to_win(race, hold_time):
    """
        Determines if you win a race at a given hold time
    """
    race_time_left = race.duration - hold_time
    return race_time_left * hold_time > race.record_length

def get_ways_to_win(race):
    """
        Returns the number of ways to win the race
        passed in
    """
    first_winning_duration, last_winning_duration = None, None
    for hold_time in range(race.duration):
        if is_way_to_win(race, hold_time):
            first_winning_duration = hold_time
            break
    
    for hold_time in range(race.duration - 1, 0, -1):
        if is_way_to_win(race, hold_time):
            last_winning_duration = hold_time
            break
        
    # plus one because inclusive
    return last_winning_duration - first_winning_duration + 1


def main(argv):
    """
        What do you think main does?
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    line_array = make_line_array(input_file_name)

    race_array = make_race_array(line_array)

    answer = 1

    for race in race_array:
        answer *= get_ways_to_win(race)

    print(answer)
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

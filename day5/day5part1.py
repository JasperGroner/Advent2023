import sys
import re
from dataclasses import dataclass

@dataclass
class ConversionRange:
    """
        To store conversion ranges
    """
    minimum: int
    maximum: int
    modifier: int

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

def get_seeds(seed_line):
    """
        Get list of seeds from first line
    """

    seeds = re.findall(r"\d+", seed_line)
    return seeds

def line_to_conversion_range(line):
    """
        Convert line to a conversion range
    """
    [destination_start, source_start, conversion_range] = re.findall(r"\d+", line)
    return ConversionRange(minimum=int(source_start), 
        maximum=int(source_start) + int(conversion_range) - 1, 
        modifier=int(destination_start) - int(source_start))

def get_conversion_range_lists(line_array):
    """
        Converts line array into conversion range
    """

    map_list = []
    current_conversion_range_list = []
    begin_map = False

    for line in line_array:
        if line.endswith("map:"):
            begin_map = True
        elif begin_map and line:
            current_conversion_range_list.append(line_to_conversion_range(line))
        elif begin_map:
            map_list.append(current_conversion_range_list)
            current_conversion_range_list = []
            begin_map = False

    #push the final map
    map_list.append(current_conversion_range_list)

    return map_list

def convert_seeds(seeds, conversion_range_lists):
    """
        Using conversion_range_list convert seeds to locations
    """
    locations = []
    for seed in seeds:
        current_number = int(seed)
        for conversion_range_list in conversion_range_lists:
            for conversion_range in conversion_range_list:
                if (conversion_range.minimum <= current_number <= conversion_range.maximum):
                    current_number += conversion_range.modifier
                    break
        locations.append(current_number)
    
    return locations
       

def main(argv):
    """
        What do you think main does?
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    line_array = make_line_array(input_file_name)

    seeds = get_seeds(line_array[0])

    conversion_range_lists = get_conversion_range_lists(line_array)

    locations = convert_seeds(seeds, conversion_range_lists)

    minimum_location = min(locations)

    print(minimum_location)
    return minimum_location

if __name__ == '__main__':
    main(sys.argv[1:])

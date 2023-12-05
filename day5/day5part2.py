from dataclasses import dataclass
import sys
import re

from day5part1 import ConversionRange, make_line_array, line_to_conversion_range, get_conversion_range_lists

@dataclass
class ItemRange:
    """
        Class to hold item range
    """
    minimum: int
    maximum: int

def get_seed_ranges(line):
    """
        Convert line into actual seed ranges
    """
    seed_ranges = []
    seed_numbers = re.findall(r"\d+", line)
    for i in range(0, len(seed_numbers), 2):
        seed_ranges.append(ItemRange(minimum=int(seed_numbers[i]), maximum=int(seed_numbers[i]) + int(seed_numbers[i + 1]) - 1))
    return seed_ranges

def range_conversion(unconverted_ranges, conversion_range):
    """
        handle a single range conversion for all unconverted ranges
    """
    converted_ranges, new_unconverted_ranges = [], []
    for input_range in unconverted_ranges:
        if conversion_range.minimum <= input_range.minimum <= conversion_range.maximum:
            if conversion_range.maximum >= input_range.maximum:
                new_range = ItemRange(minimum=input_range.minimum + conversion_range.modifier, maximum=input_range.maximum + conversion_range.modifier)
                converted_ranges.append(new_range)
            else:
                new_range = ItemRange(minimum=input_range.minimum + conversion_range.modifier, maximum=conversion_range.maximum + conversion_range.modifier)
                converted_ranges.append(new_range)
                new_unconverted_ranges.append(ItemRange(minimum=conversion_range.maximum + 1, maximum=input_range.maximum))
        elif conversion_range.minimum <= input_range.maximum <= conversion_range.maximum:
            new_range = ItemRange(minimum=conversion_range.minimum + conversion_range.modifier, maximum=input_range.maximum + conversion_range.modifier)
            converted_ranges.append(new_range)
            new_unconverted_ranges.append(ItemRange(minimum=input_range.minimum, maximum=conversion_range.minimum - 1))
        elif input_range.minimum <= conversion_range.minimum and input_range.maximum >= conversion_range.maximum:
            new_range = ItemRange(minimum=conversion_range.minimum + conversion_range.modifier, maximum=conversion_range.maximum + conversion_range.modifier)
            converted_ranges.append(new_range)
            new_unconverted_ranges.append(ItemRange(minimum=input_range.minimum, maximum=conversion_range.minimum - 1))
            new_unconverted_ranges.append(ItemRange(minimum=conversion_range.maximum + 1, maximum=input_range.maximum))
        else:
            new_unconverted_ranges.append(input_range)

    return converted_ranges, new_unconverted_ranges


def convert_seed_ranges(seed_ranges, conversion_range_lists):
    """
        Get location ranges from seed ranges and conversion lists
    """
    location_ranges = []
    new_converted_ranges = []
    # go through each set of seed ranges from input
    for seed_range in seed_ranges:
        # go through each conversion
        unconverted_ranges = [seed_range]
        for conversion_range_list in conversion_range_lists:
            # go through each conversion range
            for conversion_range in conversion_range_list:
                converted_ranges, new_unconverted_ranges = range_conversion(unconverted_ranges, conversion_range)
                new_converted_ranges.extend(converted_ranges)
                unconverted_ranges = new_unconverted_ranges
            if new_converted_ranges:
                unconverted_ranges.extend(new_converted_ranges)
            new_converted_ranges = []
        location_ranges.extend(unconverted_ranges)

    return location_ranges

def main(argv):
    """
        What do you think main does?
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    line_array = make_line_array(input_file_name)

    seed_ranges = get_seed_ranges(line_array[0])

    conversion_range_lists = get_conversion_range_lists(line_array)

    locations = convert_seed_ranges(seed_ranges, conversion_range_lists)

    minimum_locations = [location.minimum for location in locations]

    minimum_location = min(minimum_locations)

    print(minimum_location)

    return minimum_location

if __name__ == '__main__':
    main(sys.argv[1:])

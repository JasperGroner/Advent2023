import sys

def make_line_array(input_file_name: str):
    """
        Take an input file and return
        array of the lines in the file.
    """

    with open(input_file_name, 'r') as file_reader:
        raw_input = file_reader.read()
        line_array = raw_input.splitlines()

        return line_array

def digest_galaxy(galaxy_map):
    """
        Get empty rows and columns in galaxy map and locations
        of galaxies
    """
    empty_rows = list(range(0, len(galaxy_map)))
    empty_columns = list(range(0, len(galaxy_map[0])))
    galaxy_locations = []
    for y, row in enumerate(galaxy_map):
        for x, char in enumerate(row):
            if char == "#":
                if y in empty_rows:
                    empty_rows.remove(y)
                if x in empty_columns:
                    empty_columns.remove(x)
                galaxy_locations.append([x, y])
    return empty_rows, empty_columns, galaxy_locations

def adjust_galaxy_digest(galaxy_digest, empty_rows, empty_columns):
    """Adjust for universe expansion"""
    for galaxy in galaxy_digest:
        for idx, col in enumerate(empty_columns):
            if col > galaxy[0]:
                galaxy[0] += idx
                break
            if idx == len(empty_columns) - 1:
                galaxy[0] += (idx + 1)
        for idx, row in enumerate(empty_rows):
            if row > galaxy[1]:
                galaxy[1] += idx
                break
            if idx == len(empty_rows) - 1:
                galaxy[1] += (idx + 1)
    return galaxy_digest

def get_distance_sums(adjusted_digest):
    """
        get sum of distances between all galaxies in map
    """
    total = 0
    for idx, source in enumerate(adjusted_digest):
        for dest in adjusted_digest[idx + 1:]:
            total += abs(dest[0] - source[0])
            total += abs(dest[1] - source[1])
    return total


def main(argv):
    """
        What do you think main does?
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    galaxy_map = make_line_array(input_file_name)

    empty_rows, empty_columns, galaxy_digest = digest_galaxy(galaxy_map)

    adjusted_digest = adjust_galaxy_digest(galaxy_digest, empty_rows, empty_columns)

    answer = get_distance_sums(adjusted_digest)

    print(answer)
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

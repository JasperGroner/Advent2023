import sys

def check_line(line, num_red, num_green, num_blue):
    colon_split_line = line.split(":")
    line_num = int(colon_split_line[0][5:])
    cube_group_sets = colon_split_line[1].split(";")
    for cube_group_set in cube_group_sets:
        red, green, blue = 0, 0, 0
        cube_groups = cube_group_set.split(",")
        for cube_group in cube_groups:
            cube_group = cube_group.strip()
            [number, cube_type] = cube_group.split(" ")
            if cube_type == "red":
                red += int(number)

            elif cube_type == "green":
                green += int(number)
            else:
                blue += int(number)
            if red > num_red or green > num_green or blue > num_blue:
                return 0
    return line_num

def main(argv):
    if (len(argv) < 4):
        print("Please include input file and max red, green, and blue as arguments.")
        return
    input_file_name = argv[0]
    num_red, num_green, num_blue = int(argv[1]), int(argv[2]), int(argv[3])
    file_reader = open(input_file_name, 'r')
    input_text = file_reader.read()
    line_num_sum = 0
    for line in input_text.splitlines():
        line_num_sum += check_line(line, num_red, num_green, num_blue)
    print(line_num_sum)

if __name__ == '__main__':
    main(sys.argv[1:])

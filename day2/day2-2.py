import sys

def check_line(line):
    colon_split_line = line.split(":")
    line_num = int(colon_split_line[0][5:])
    cube_group_sets = colon_split_line[1].split(";")
    min_red, min_green, min_blue = 0, 0, 0
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
        min_red = red if red > min_red else min_red
        min_green = green if green > min_green else min_green
        min_blue = blue if blue > min_blue else min_blue
    return min_red * min_green * min_blue

def main(argv):
    if (len(argv) < 1):
        print("Please include input file.")
        return
    input_file_name = argv[0]
    file_reader = open(input_file_name, 'r')
    input_text = file_reader.read()
    line_power_sum = 0
    for line in input_text.splitlines():
        line_power_sum += check_line(line)
    print(line_power_sum)

if __name__ == '__main__':
    main(sys.argv[1:])

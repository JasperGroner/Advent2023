import sys
import re
import math

from day8part1 import make_line_array, get_map

non_z_ending = re.compile(r'[^Z]$')
z_ending = re.compile(r'Z$')

def get_starting_nodes(node_map):
    """
        Get all nodes whose location ends in "A"
    """
    starting_nodes = [node_id for node_id in node_map.keys() if node_id.endswith("A")]
    return starting_nodes

def get_number_of_z_loops(instructions, node_map, start):
    """
        Get number of steps to traverse node_map using instructions
    """
    current = start
    steps = 0
    num_instructions = len(instructions)
    z_ending_locations = {}

    while(True):
        if z_ending.search(current):
            if current in z_ending_locations:
                break
            z_ending_locations[current] = steps
        next_turn = instructions[steps % num_instructions]
        current = node_map[current].L if next_turn == 'L' else node_map[current].R
        steps += 1

    return list(z_ending_locations.values())

def get_number_of_steps(instructions, node_map):
    """
        Get number of steps to traverse node_map using instructions
    """
    current_nodes = get_starting_nodes(node_map)
    loop_lengths = []
    for node in current_nodes:
        loop_lengths += get_number_of_z_loops(instructions, node_map, node)

    return math.lcm(*loop_lengths)

def main(argv):
    """
        What do you think main does?
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    [instructions, _, *nodes] = make_line_array(input_file_name)

    node_map = get_map(nodes)

    answer = get_number_of_steps(instructions, node_map)


    print(answer)
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

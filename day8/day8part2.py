import sys
import re

from day8part1 import make_line_array, get_map

z_ending = re.compile(r'[^Z]$')

def get_starting_nodes(node_map):
    """
        Get all nodes whose location ends in "A"
    """
    starting_nodes = [node_id for node_id in node_map.keys() if node_id.endswith("A")]
    return starting_nodes

def get_number_of_steps(instructions, node_map):
    """
        Get number of steps to traverse node_map using instructions
    """
    current_nodes = get_starting_nodes(node_map)
    steps = 0
    num_instructions = len(instructions)
    while ((num_non_zs := len([node for node in current_nodes if z_ending.search(node)])) > 0):
        if num_non_zs < len(current_nodes) - 2:
            print(num_non_zs, steps)
        next_turn = instructions[steps % num_instructions]
        for idx, node in enumerate(current_nodes):
            current_nodes[idx] = node_map[node].L if next_turn == 'L' else node_map[node].R
        steps += 1

    return steps


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

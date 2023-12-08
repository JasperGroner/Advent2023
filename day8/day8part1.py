from dataclasses import dataclass
import sys

@dataclass
class MapNode:
    """
        Store map nodes
    """
    L: str
    R: int

def make_line_array(input_file_name):
    """
        Take an input file and return
        array of the lines in the file.
    """

    file_reader = open(input_file_name, 'r')
    raw_input = file_reader.read()
    line_array = raw_input.splitlines()

    file_reader.close()
    return line_array


def get_map(nodes):
    """
        return map of desert nodes
    """
    node_map = {}

    for node in nodes:
        [identity, next_loc] = node.split(" = ")
        [L, R] = next_loc.strip("()").split(", ")
        node_map[identity] = MapNode(L, R)

    return node_map

def get_number_of_steps(instructions, node_map):
    """
        Get number of steps to traverse node_map using instructions
    """
    current = "AAA"
    steps = 0
    num_instructions = len(instructions)

    while(current != "ZZZ"):
        next_turn = instructions[steps % num_instructions]
        current = node_map[current].L if next_turn == 'L' else node_map[current].R
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

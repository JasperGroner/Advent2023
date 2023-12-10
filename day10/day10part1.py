import sys

EXITS = {
    "|": ["+y", "-y"],
    "-": ["+x", "-x"],
    "L": ["-y", "+x"],
    "J": ["-y", "-x"],
    "7": ["+y", "-x"],
    "F": ["+y", "+x"],
    ".": [],
}

class Pipe:
    """
        Stores openings from a given pipe.
    """

    def __init__(self, x: int, y: int, char: str):
        self.prev_pipe = {}
        self.next_pipe = {}
        self.location = {"x": x, "y": y}
        self.char = char

    def set_prev_pipe(self,  prev_x: int, prev_y: int):
        self.prev_pipe = {"x": prev_x, "y": prev_y}

    def get_next_pipe(self):
        pipe1, pipe2 = self.get_adjoining_pipes()
        self.next_pipe = pipe1 if pipe2 == self.prev_pipe else pipe2
    
    def get_adjoining_pipes(self):
        if (self.char == "." or self.char == "S"):
            print(self.char)
            return None
        exits = EXITS[self.char]
        [pipe1, pipe2] = [self.translate_map_char(exit_loc) for exit_loc in exits]
        return pipe1, pipe2

    def translate_map_char(self, char:str):
        if char.endswith("x"):
            if char.startswith("+"):
                return {"x": self.location["x"] + 1, "y": self.location["y"]}
            return {"x": self.location["x"] - 1, "y": self.location["y"]}
        else:
            if char.startswith("+"):
                return {"x": self.location["x"], "y": self.location["y"] + 1}
            return {"x": self.location["x"], "y": self.location["y"] - 1}

        
def make_line_array(input_file_name: str):
    """
        Take an input file and return
        array of the lines in the file.
    """

    with open(input_file_name, 'r') as file_reader:
        raw_input = file_reader.read()
        line_array = raw_input.splitlines()

        return line_array

def find_start(line_array):
    for y, line in enumerate(line_array):
        for x, char in enumerate(line):
            if char == 'S':
                return y, x

def get_first_steps(line_array, start_y, start_x):
    start_location = {"y": start_y, "x": start_x}
    first_steps = []
    adjoining_locations = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for location in adjoining_locations:
        adjoining_pipe = Pipe(start_x + location[1], start_y + location[0],
            line_array[start_y + location[0]][start_x + location[1]])
        pipe_adj_loc = adjoining_pipe.get_adjoining_pipes()
        if line_array[start_y + location[0]][start_x + location[1]] != '.' and \
                start_location in pipe_adj_loc:
            first_steps.append(Pipe(start_x + location[1], start_y + location[0],
                line_array[start_y + location[0]][start_x + location[1]]))

    for pipe in first_steps:
        pipe.set_prev_pipe(start_x, start_y)
        pipe.get_next_pipe()
    return first_steps

def get_answer(line_array, pipes):
    # start with one step, since we're one from start
    answer = 1
    while (pipes[0].location["x"] != pipes[1].location["x"] or \
            pipes[0].location["y"] != pipes[1].location["y"]):
        for idx, pipe in enumerate(pipes):
            prev_x, prev_y = pipe.location["x"], pipe.location["y"]
            pipes[idx] = Pipe(x = pipe.next_pipe["x"], y = pipe.next_pipe["y"],
                char = line_array[pipe.next_pipe["y"]][pipe.next_pipe["x"]])
            pipes[idx].set_prev_pipe(prev_x, prev_y)
            pipes[idx].get_next_pipe()
        answer += 1
    # increment once more for final step
    return answer

def main(argv):
    """
        What do you think main does?
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    line_array = make_line_array(input_file_name)

    start_y, start_x = find_start(line_array)

    first_steps = get_first_steps(line_array, start_y, start_x)

    answer = get_answer(line_array, first_steps)

    print(answer)
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

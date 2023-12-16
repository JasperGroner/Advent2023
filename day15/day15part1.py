import sys

def get_inputs(input_file_name: str) -> list[str]:
    """
        Take an input file and return
        array of the lines in the file.
    """

    with open(input_file_name, 'r') as file_reader:
        raw_input = file_reader.read()
        input_array = raw_input[:-1].split(",")

        return input_array

def hash_input(unhashed: str) -> int:
    """
        Ush HASH algorithm to turn raw input into number
    """
    hashed = 0
    for char in unhashed:
        hashed += ord(char)
        hashed *= 17
        hashed %= 256

    return hashed

def main(argv: list[str]) -> int:
    """
        it's main it does the main stuffd
    """
    if len(argv) < 1:
        print("Please include file input")
        return

    input_file_name = argv[0]

    inputs = get_inputs(input_file_name)
    
    answer = 0

    for unhashed in inputs:
        answer += hash_input(unhashed)

    print("answer: " + str(answer))
    return answer

if __name__ == '__main__':
    main(sys.argv[1:])

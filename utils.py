def read_puzzle_input(path: str):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
        return lines
def parse_intcode_program(filename):
    with open(filename, "r") as f:
        return list(map(int, f.readlines()[0][:-1].split(',')))

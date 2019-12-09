from intcode import parse_intcode_program

def parse_instruction(val):
    str_val = str(val)
    params = [0, 0, 0]  # using 3 parameters
    # In case we use legacy OP format from Day 2
    if len(str_val) == 1:
        return val, params
    # Day 5 OP formats
    op = int(str_val[-2:])
    for i, p in enumerate(str_val[:-2][::-1]):
        params[i] = int(p)
    return op, params


def parse_mode(program, parameters, param_index, pos):
    if parameters[param_index] == 0:      # position mode
        return program[program[pos+1]]
    elif parameters[param_index] == 1:    # immediate mode
        return program[program+1]
    elif parameters[param_index] == 2:    # relative mode
        pass
    else:
        raise Exception('Illegal mode!. The value was: {}'.format(op))


def parse_program(prog, inp=[], i=0):
    prog_output = None

    while True:
        # get the OP and its parameters
        op, params = parse_instruction(prog[i])
        # termination
        if op == 99:
            # support for changes inputs in day7
            return prog, None, i
        # adition
        elif op == 1:
            val1 = prog[i+1] if params[0] == 1 else prog[prog[i+1]]
            val2 = prog[i+2] if params[1] == 1 else prog[prog[i+2]]
            # writing always in position mode (here and thereafter)
            prog[prog[i+3]] = val1 + val2
            i += 4
        # multiplication
        elif op == 2:
            val1 = prog[i+1] if params[0] == 1 else prog[prog[i+1]]
            val2 = prog[i+2] if params[1] == 1 else prog[prog[i+2]]
            prog[prog[i+3]] = val1 * val2
            i += 4
        # input
        elif op == 3:
            # support for mulitple inputs in day7
            prog[prog[i+1]] = inp.pop(0)
            i += 2
        # output
        elif op == 4:
            prog_output = prog[i+1] if params[0] == 1 else prog[prog[i+1]]
            i += 2
            # support for changes inputs in day7
            return prog[:], prog_output, i
        # jump-if-true
        elif op == 5:
            val1 = prog[i+1] if params[0] == 1 else prog[prog[i+1]]
            if val1 != 0:
                i = prog[i+2] if params[1] == 1 else prog[prog[i+2]]
            else:
                i += 3
        # jump-if-false
        elif op == 6:
            val1 = prog[i+1] if params[0] == 1 else prog[prog[i+1]]
            if val1 == 0:
                i = prog[i+2] if params[1] == 1 else prog[prog[i+2]]
            else:
                i += 3
        # less-than
        elif op == 7:
            val1 = prog[i+1] if params[0] == 1 else prog[prog[i+1]]
            val2 = prog[i+2] if params[1] == 1 else prog[prog[i+2]]
            prog[prog[i+3]] = 1 if val1 < val2 else 0
            i += 4
        # equals
        elif op == 8:
            val1 = prog[i+1] if params[0] == 1 else prog[prog[i+1]]
            val2 = prog[i+2] if params[1] == 1 else prog[prog[i+2]]
            prog[prog[i+3]] = 1 if val1 == val2 else 0
            i += 4
        # invalid input
        else:
            raise Exception('Illegal OPCODE. The value was: {}'.format(op))

if __name__ == '__main__':
    program  = parse_intcode_program("inputs/day5.txt")

    program_input = [5]
    _, result, _ = parse_program(program, program_input)

    print("Part 1 and/or 2 Answer:", result)

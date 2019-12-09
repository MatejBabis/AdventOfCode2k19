from intcode import parse_intcode_program
from day5 import parse_program
from itertools import permutations

# Read in the program
program  = parse_intcode_program("inputs/day7.txt")

max_signal = (float('-inf'), None)
for permutation in permutations(range(5)):
    program_input = 0

    for p in permutation:
        _, program_output, _ = parse_program(program, [p, program_input])

        if max_signal[0] < program_output:
            max_signal = (program_output, permutation)
        program_input = program_output

print("Part 1 Answer: %d %s" % (max_signal[0], max_signal[1]))

max_signal = (float('-inf'), None)
for perm in permutations(range(5,10)):
    # initialize arrays for each amplifier
    pointers = [0] * len(perm)
    outputs = [0] * len(perm)
    instructions = [program[:]] * len(perm)
    input_queue = [[perm[i]] for i in range(len(perm))]
    # ad 0 as the first instruction to the first amplifier
    input_queue[0].append(0)

    amp = 0
    while True:
        instructions[amp], output, pointer_new = parse_program(instructions[amp],
                                                               input_queue[amp],
                                                               pointers[amp])
        # one of the amplifiers has encountered 99
        if output is None:
            # if the last output (max thruster signal) beats the current max
            if outputs[-1] > max_signal[0]:
                max_signal = outputs[-1], perm
            # terminate execution
            break
        # update values
        pointers[amp] = pointer_new
        outputs[amp] = output
        # ensure we only cycle the 5 amplifiers we have
        input_queue[(amp + 1) % 5].append(output)
        amp = (amp + 1) % 5

print("Part 2 Answer: %d %s" % (max_signal[0], max_signal[1]))

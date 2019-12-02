def compute(x):
    i = 0
    while True:
        if x[i] == 1: x[x[i+3]] = x[x[i+1]] + x[x[i+2]]
        elif x[i] == 2: x[x[i+3]] = x[x[i+1]] * x[x[i+2]]
        elif x[i] == 99: return x
        else: raise Exception('Illegal OPCODE. The value was: {}'.format(x[i]))
        i += 4

# part 1
with open("inputs/day2.txt", "r") as f:
    # parse input into a list of ints
    opcodes = list(map(int, f.readlines()[0][:-1].split(',')))

    # replace as per instructions
    opcodes[1] = 12
    opcodes[2] = 2
    result = compute(opcodes)

print("Part 1 Answer: %d" % result[0])


# part 2
with open("inputs/day2.txt", "r") as f:
    # parse input into a list of ints
    x = list(map(int, f.readlines()[0][:-1].split(',')))
    target = 19690720   # given input
    # create a list clone to revert list state after each loop iteration
    x_orig = x.copy()

# use small values to try and find a pattern
for noun in range(3):
    for verb in range(3):
        x[1] = noun
        x[2] = verb
        i = 0
        while True:
            if x[i] == 1: x[x[i+3]] = x[x[i+1]] + x[x[i+2]]
            elif x[i] == 2: x[x[i+3]] = x[x[i+1]] * x[x[i+2]]
            elif x[i] == 99:
                print(noun, verb, x[0])
                break
            else: raise Exception('Illegal OPCODE. The value was: {}'.format(x[i]))
            i += 4
        # revert back to original state
        x = x_orig.copy()

# discovered a pattern by looping:
#   noun=0, verb=0 yield `base` value
#       * increasing noun by 1 increases x[0]_{i} by `diff` from x[0]_{i-1}
#       * increasing verb by 1 increases x[0]_{i} by 1 from x[0]_{i-1}
#   with that, we can compute the noun, verb for the target given:
#       * noun = (target - base) / diff (rounded down to nearest int)
#       * verb = target - (noun * diff + base)
base = compute(x[:1] + [0] + x[2:])[0]
diff = compute(x[:1] + [1] + x[2:])[0] - compute(x[:1] + [0] + x[2:])[0]
target_noun = (target - base) // diff
target_verb = target - (target_noun * diff + base)

print("Part 2 Answer: %d" % (100 * target_noun + target_verb))

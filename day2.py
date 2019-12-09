from intcode import parse_intcode_program

from day5 import parse_program as compute

# part 1
opcodes = parse_intcode_program("inputs/day2.txt")

# replace as per instructions
opcodes[1] = 12
opcodes[2] = 2
result = compute(opcodes)

print("Part 1 Answer: %d" % result[0][0])

# part 2
x  = parse_intcode_program("inputs/day2.txt")
target = 19690720   # given input
# create a list clone to revert list state after each loop iteration
x_orig = x.copy()

# use small values to try and find a pattern
for noun in range(3):
    for verb in range(3):
        x[1] = noun
        x[2] = verb
        x = compute(x)
        # revert back to original state
        x = x_orig.copy()

# discovered a pattern by looping:
#   noun=0, verb=0 yield `base` value
#       * increasing noun by 1 increases x[0]_{i} by `diff` from x[0]_{i-1}
#       * increasing verb by 1 increases x[0]_{i} by 1 from x[0]_{i-1}
#   with that, we can compute the noun, verb for the target given:
#       * noun = (target - base) / diff (rounded down to nearest int)
#       * verb = target - (noun * diff + base)
base = compute(x[:1] + [0] + x[2:])[0][0]
diff = compute(x[:1] + [1] + x[2:])[0][0] - compute(x[:1] + [0] + x[2:])[0][0]
target_noun = (target - base) // diff
target_verb = target - (target_noun * diff + base)

print("Part 2 Answer: %d" % (100 * target_noun + target_verb))

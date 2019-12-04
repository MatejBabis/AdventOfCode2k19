from itertools import islice
from operator import eq


def check_adj(n_str):
    # `islice()` slices a sequence
    # `map & eq` checks if an item in the sequence is
    #   the same as the following item in the sequence
    # returns a list of True\False values if an adjacent
    # pair of the same value exists
    return list(map(eq, n_str, islice(n_str, 1, None)))


def check_incr(n_str):
    # check if the last two digits adhere to the increasing condition
    if int(n_str[-2]) > int(n_str[-1]):
        return False
    # none of the numbers breaks the increasing condition
    if len(n_str) == 2:
        return True
    # recursive check for string without the last digit
    return check_incr(n_str[:-1])

# WARNING: Ugly function for part 2
# given the output of `check_adj()`, check if at least one `True`
# value that is not adjacent to another `True` value exists
def single_pair_exists(array):
    # edge case: "[True, False, ...]"
    if array[0] is True and array[1] is False:
        return True
    # sliding window looking for "[..., False, True, False, ...]"
    for i in range(1, len(array)-1):
        if array[i-1] is False and array[i] is True and array[i+1] is False:
            return True
    # edge case: "[..., False, True]"
    if array[len(array)-2] is False and array[len(array)-1] is True:
        return True
    # no single pair value exists
    return False


INPUT_RANGE = range(138307, 654504)

p1_valid_pws = 0
p2_valid_pws = 0
for x in INPUT_RANGE:
    str_x = str(x)
    increasing = check_incr(str_x)
    # part 1 answer
    if increasing and True in check_adj(str_x):
        p1_valid_pws += 1
    # part 2 answer
    if increasing and single_pair_exists(check_adj(str_x)):
        p2_valid_pws += 1

print("Part 1 Answer:", p1_valid_pws)
print("Part 2 Answer:", p2_valid_pws)

from collections import defaultdict


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dir_vector(m):
    if m[0] == 'R': return (int(m[1:]), 0)
    elif m[0] == 'L': return (-int(m[1:]), 0)
    elif m[0] == 'U': return (0, int(m[1:]))
    elif m[0] == 'D': return (0, -int(m[1:]))
    else: raise Exception("Invalid instruction '{}'".format(m))


def draw_wire(b, s, w, name='w1'):
    x, y = 0, 0
    steps = 0
    for move in w:
        for _ in range(abs(sum(move))):
            steps += 1
            if move[0] == 0:            # moving up or down
                if move[1] > 0: y += 1  # moving up
                else: y -= 1            # moving down
            else:                       # moving right or left
                if move[0] > 0: x +=1   # moving right
                else: x -= 1            # moving left

            # count how long it took to get to this location
            if s[(x,y)] == -1:
                s[(x,y)] = steps

            # empty piece on the board (or occupied by this wire)
            if b[(x,y)] == "." or b[(x,y)] == name:
                b[(x,y)] = name
            # a different wire already went through here -> crossing
            else:
                b[(x,y)] = 'X'

    return board, s


wires = []
with open("inputs/day3.txt", "r") as f:
    # parse input into a list of ints
    for line in f.readlines():
        wire_path = []
        instructions = line[:-1].split(',')
        for move in instructions:
            wire_path.append(dir_vector(move))
        wires.append(wire_path)

w1, w2 = wires
board = defaultdict(lambda: '.')
w1_steps = defaultdict(lambda: -1)
w2_steps = defaultdict(lambda: -1)

central = (0,0)
board[central] = 'o' # central
w1_steps[central] = 0
w2_steps[central] = 0

# wire1
board, w1_steps = draw_wire(board, w1_steps, w1, name='w1')
# wire2
board, w2_steps = draw_wire(board, w2_steps, w2, name='w2')

# find crossings and compute the shortest manhattan distance
min_dist = 999999999
steps_to_crossing = defaultdict(lambda: -1)
for coords, v in board.items():
    if v == 'X':
        dist = manhattan((0, 0), coords)
        if dist < min_dist:
            min_dist = dist
        steps_to_crossing[coords] = w1_steps[coords] + w2_steps[coords]

print("Part 1 Answer:", min_dist)
print("Part 2 Answer:", min(steps_to_crossing.values()))

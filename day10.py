import numpy as np
from collections import defaultdict, OrderedDict

# returns signed clockwise angular difference
def angle_between(p1, p2):
    ang1 = np.arctan2(*p1)
    ang2 = np.arctan2(*p2)
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

def distance_between(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


asteroids = []
with open("inputs/day10.txt") as f:
    for y, line in enumerate(f.readlines()):
        line = line.split()[0]
        for x, symb in enumerate(line):
            if symb == "#":
                asteroids += [(x,y)]

max_coords = None, None
max_visible = 0
max_asteroid_data = None

for pivot in asteroids:
    asteroid_data = defaultdict()
    for a in asteroids:
        if pivot == a:
            continue
        # we need to shift the asteroids (x,y) based on the pivot's (x,y)
        # so that the pivot appears to be the origin (0,0)
        angle = angle_between((0, 0),
                              (pivot[0] - a[0], pivot[1] - a[1]))
        # calculate the distance between pivot and asteroid
        distance = distance_between(pivot, a)
        asteroid_data[a] = (angle, distance)
        # count the number of unique angles == visible asteroids
        visible = np.unique([a for a, d in asteroid_data.values()])

    if len(visible) > max_visible:
        max_coords, max_visible = pivot, len(visible)
        # for part2
        max_asteroid_data = asteroid_data.copy()

print("Part 1 Answer: %s with %d visible" % (max_coords, max_visible))

# create a separate queue for each unique angle value
angle_queue = defaultdict(list)
for coord, (angle, distance) in max_asteroid_data.items():
    angle_queue[angle] += [(coord, distance)]
    # sort the queue based on distance from the pivot
    angle_queue[angle] = sorted(angle_queue[angle], key=lambda tup: tup[1])

destroying = True
destroyed_ctr = 0
winner_coords = (None, None)

while destroying:
    # consider angles in the clockwise direction (starting from 12 o'clock)
    line_of_sight_angles = sorted(angle_queue.keys())
    for angle in line_of_sight_angles:
        destroyed_ctr += 1
        # store information when we have found the winner
        if destroyed_ctr == 200:
            destroying = False
            winner_coords = angle_queue[angle][0][0]
            break

        # remove the head of the queue
        angle_queue[angle] = angle_queue[angle][1:]
        # if that made the queue empty, completely remove the angle listing
        if angle_queue[angle] == []:
            del angle_queue[angle]

print("Part 2 Answer: %d" % (winner_coords[0] * 100 + winner_coords[1]))

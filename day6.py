from collections import defaultdict


# Find the shortest path between two vertices using BFS
def bfs_shortest_path(graph, start, goal):
    if start == goal:
        return []

    visited = set()
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            # shallow copy needed because of how python handles sets in memory
            orbit_centers = graph[node].copy()
            # need to remove the start node as this is a bidirectional
            # graph and traversal might get stuck in an infinite loop
            if start in orbit_centers:
                orbit_centers.remove(start)
            for oc in orbit_centers:
                queue.append(path + [oc])
                if oc == goal:
                    # return the path without the start node
                    return [v for v in path + [oc] if v != start]
            visited.add(node)


orbits = defaultdict(set)

# Read in the program
with open("inputs/day6.txt", "r") as f:
    # parse the input into relations
    for relation in f.readlines():
        orbit_center, satellite = relation[:-1].split(')')
        # bidirectional graph, so add "s:o" as well as "o:s"
        orbits[satellite].add(orbit_center)
        orbits[orbit_center].add(satellite)

total_orbits = 0
for satellite in orbits.keys():
    total_orbits += len(bfs_shortest_path(orbits, satellite, 'COM'))

print('Part 1 Answer:', total_orbits)

# subtract 1 because we only want to get to the object 'SAN' is orbitting &&
# subtract 1 because we are interested in the number of edges, not vertices
p2_answer = len(bfs_shortest_path(orbits, 'YOU', 'SAN')) -1 -1
print('Part 2 Answer:', p2_answer)

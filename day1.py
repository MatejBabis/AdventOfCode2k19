# part 1
with open("inputs/day1.txt", "r") as f:
    total_fuel = 0
    for line in f.readlines():
        x = int(line[:-1])  # remove '\n' and cast to int
        x_mass = x // 3 - 2
        total_fuel += x_mass

    print("Part1 Answer:", total_fuel)

# part 2
with open("inputs/day1.txt", "r") as f:
    total_fuel = 0
    for line in f.readlines():
        x = int(line[:-1])  # remove '\n' and cast to int
        while True:
            x_mass = x // 3 - 2
            if x_mass < 1: break
            total_fuel += x_mass
            x = x_mass

    print("Part2 Answer:", total_fuel)

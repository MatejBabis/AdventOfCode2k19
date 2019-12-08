import numpy as np

# print numpy array without any extra notation
def numpy_print(a):
    print('\n'.join(''.join(str(cell) for cell in row) for row in a))

with open("inputs/day8.txt", "r") as f:
    raw_image = f.readline()[:-1]

dim = (6,25) # (rows, col_size)

layer_size = dim[0] * dim[1]
raw_layers = [raw_image[i:layer_size+i] for i in range(0,len(raw_image), layer_size)]

min_zeros = float('inf')
p1_result = None                        # answer container for p1
image = np.array([2] * layer_size)      # answer container for p2
for raw_layer in raw_layers:
    # PART1
    # convert to numpy array of ints
    layer = np.array(list(map(int, raw_layer)))
    # count occurrence of each number in the layer
    unique, counts = np.unique(layer, return_counts=True)
    occurrence = dict(zip(unique, counts))

    if occurrence[0] < min_zeros:
        p1_result = occurrence[1] * occurrence[2]
        min_zeros = occurrence[0]

    # PART2
    # numpy conditional to iteratively update image values
    image = np.where((image == 2) & (layer != 2), layer, image)

print("Part 1 Answer:", p1_result)
print("Part 2 Answer:")
numpy_print(image.reshape(dim))

def get_layers():
    image_width = 25
    image_height = 6
    number_of_digits_per_layer = image_height * image_width

    layers = []

    file = open('input', "r+")
    puzzle_input = file.readline()
    file.close()

    layers.append([])

    for i in range(len(puzzle_input)):
        layers[-1].append(puzzle_input[i])
        if len(layers[-1]) % number_of_digits_per_layer == 0:
            layers.append([])

    layers.pop(-1)

    return layers


def get_solution_to_problem_1():
    layers = get_layers()
    fewest_digits_layer = layers[0]

    for layer in layers:
        if layer.count('0') < fewest_digits_layer.count('0'):
            fewest_digits_layer = layer

    print(f"Solution to problem 1 is: {fewest_digits_layer.count('1') * fewest_digits_layer.count('2')}.")


def get_solution_to_problem_2():
    layers = get_layers()
    image_width = 25
    visible_image = [[]]

    for i in range(len(layers[0])):  # For each pixel
        for j in range(len(layers)):  # In each layer
            # Get first pixel that is not transparent, then break
            if layers[j][i] == '2':
                continue
            visible_image[-1].append(layers[j][i])
            if len(visible_image[-1]) == image_width:
                visible_image.append([])
            break

    for row in visible_image:

        print(''.join(row).replace('0', ' '))


get_solution_to_problem_1()
get_solution_to_problem_2()

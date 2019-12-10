class GeometricLine:

    def __init__(self):
        self.a = 0
        self.b = 0


def get_solution_to_problem_1():
    space_map = get_space_map_from_input('test1')
    print(space_map[1][0])


def get_space_map_from_input(input_path):
    file = open(input_path)
    lines = file.readlines()
    file.close()

    space_map = []

    for line in range(len(lines)):
        space_map.append([])

    for i in range(len(lines[0])):
        for j in range(len(lines)):
            space_map[j].append(line[i][j])

    return space_map



get_solution_to_problem_1()
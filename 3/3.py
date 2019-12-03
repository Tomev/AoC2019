from math import fabs


class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


def count_manhattan_distance(p1: Point, p2: Point):
    return fabs(p1.x - p2.x) + fabs(p1.y - p2.y)


def find_solution_to_problem_1(input_file):
    #  I will assume, that the central port is in position (0,0)
    file = open(input_file, "r+")
    lines = file.readlines()
    file.close()

    first_wire_positions = get_positions_from_string(lines[0])
    second_wire_positions = get_positions_from_string(lines[1])

    intersections = list(set(first_wire_positions) & set(second_wire_positions))

    central_port_position = Point(0, 0)
    closest_intersection_distance = count_manhattan_distance(central_port_position, intersections[0])

    for i in range(1, len(intersections)):
        intersection_distance = count_manhattan_distance(central_port_position, intersections[i])

        if intersection_distance < closest_intersection_distance:
            closest_intersection_distance = intersection_distance

    print(f'Closest intersection distance is {closest_intersection_distance}.')


def get_positions_from_string(string: str):
    actions = string.split(',')
    current_position = Point(0, 0)  # Assumption
    positions = []

    for action in actions:
        movement_direction = action[0]
        movement_distance = int(action[1:len(action)])

        if movement_direction == 'R':
            positions += get_right_path(current_position, movement_distance)
        if movement_direction == 'L':
            positions += get_left_path(current_position, movement_distance)
        if movement_direction == 'U':
            positions += get_up_path(current_position, movement_distance)
        if movement_direction == 'D':
            positions += get_down_path(current_position, movement_distance)

        current_position = positions[len(positions) - 1]

    return positions


def get_right_path(current_position: Point, movement_distance: int):
    path = []

    for i in range(movement_distance):
        current_position = Point(current_position.x + 1, current_position.y)
        path.append(current_position)

    return path


def get_down_path(current_position: Point, movement_distance: int):
    path = []

    for i in range(movement_distance):
        current_position = Point(current_position.x, current_position.y - 1)
        path.append(current_position)

    return path


def get_up_path(current_position: Point, movement_distance: int):
    path = []

    for i in range(movement_distance):
        current_position = Point(current_position.x, current_position.y + 1)
        path.append(current_position)

    return path


def get_left_path(current_position: Point, movement_distance: int):
    path = []

    for i in range(movement_distance):
        current_position = Point(current_position.x - 1, current_position.y)
        path.append(current_position)

    return path


def find_solution_to_problem_2(input_file):
    #  I will assume, that the central port is in position (0,0)
    file = open(input_file, "r+")
    lines = file.readlines()
    file.close()

    first_wire_positions = get_positions_from_string(lines[0])
    second_wire_positions = get_positions_from_string(lines[1])

    intersections = list(set(first_wire_positions) & set(second_wire_positions))

    shortest_wire_path = first_wire_positions.index(intersections[0]) + second_wire_positions.index(intersections[0]) + 2

    for i in range(1, len(intersections)):
        wire_path = first_wire_positions.index(intersections[i]) + second_wire_positions.index(intersections[i]) + 2

        if wire_path < shortest_wire_path:
            shortest_wire_path = wire_path

    print(f'Shortest wire path is {shortest_wire_path}.')


# find_solution_to_problem_1('test0.txt')
# find_solution_to_problem_1('test1.txt')
# find_solution_to_problem_1('test2.txt')
# find_solution_to_problem_1('input1.txt')

find_solution_to_problem_2('test0.txt')
find_solution_to_problem_2('test1.txt')
find_solution_to_problem_2('test2.txt')
find_solution_to_problem_2('input1.txt')

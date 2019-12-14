from std import Point, get_program_from_input
from ship import ShipComputer


class Tile:

    def __init__(self, position: Point):
        self.position = position
        self.color = 0

    def __eq__(self, o):
        return self.position == o.position


def get_traveled_tiles(start_tile: Tile):
    program = get_program_from_input('input')
    computer = ShipComputer()
    computer.set_program(program)
    directions = ['U', 'R', 'D', 'L']
    movements = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]
    direction = 'U'
    current_tile = start_tile

    traveled_tiles = []

    while not computer.program_finished:

        if not traveled_tiles.__contains__(current_tile):
            traveled_tiles.append(current_tile)
        else:
            current_tile = traveled_tiles[traveled_tiles.index(current_tile)]

        computer.input.append(current_tile.color)
        computer.run_program()

        # Coloring
        current_tile.color = computer.outputs[-2]

        # Rotating
        if computer.outputs[-1] == 0:  # Turn left
            direction = directions[directions.index(direction) - 1]
        else:
            direction = directions[(directions.index(direction) + 1) % len(directions)]

        new_position = current_tile.position
        new_position += movements[directions.index(direction)]

        current_tile = Tile(new_position)

    return traveled_tiles


def get_solution_to_problem_1():
    current_tile = Tile(Point(0, 0))
    traveled_tiles = get_traveled_tiles(current_tile)
    print(len(traveled_tiles))


def get_solution_to_problem_2():
    current_tile = Tile(Point(0, 0))
    current_tile.color = 1
    traveled_tiles = get_traveled_tiles(current_tile)

    max_y = min_y = traveled_tiles[0].position.y
    max_x = min_x = traveled_tiles[0].position.x

    for tile in traveled_tiles:
        if tile.position.y > max_y:
            max_y = tile.position.y
        if tile.position.y < min_y:
            min_y = tile.position.y
        if tile.position.x > max_x:
            max_x = tile.position.x
        if tile.position.x < min_x:
            min_x = tile.position.x

    registration_identifier = []
    for y in range(max_y - min_y + 1):
        registration_identifier.append([' ' for x in range(max_x - min_x + 1)])

    for tile in traveled_tiles:
        if tile.color == 1:
            registration_identifier[tile.position.y - min_y][tile.position.x - min_x] = 'X'

    registration_identifier.reverse()

    for line in registration_identifier:
        print(''.join(line))


get_solution_to_problem_1()
get_solution_to_problem_2()





